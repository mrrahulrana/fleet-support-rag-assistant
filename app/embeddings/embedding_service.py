import os
import warnings
from typing import Optional, List, Callable
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings
from dotenv import load_dotenv

# Suppress HF warnings before importing HF-based things
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
warnings.filterwarnings("ignore", message=".*You are sending unauthenticated requests to the HF Hub.*")
warnings.filterwarnings("ignore", message=".*huggingface_hub.*cache-system uses symlinks.*")

load_dotenv()

_OPENAI_FALLBACK_TO_LOCAL = False

def _get_use_local_from_env() -> bool:
    val = os.getenv("USE_LOCAL_EMBEDDINGS", "false").strip().lower()
    return val in ("true", "1", "yes", "on")


class FallbackEmbeddings(Embeddings):
    """
    Embeddings wrapper that:
      - Uses OpenAI by default.
      - Automatically falls back to local HuggingFace embeddings when OpenAI
        raises a quota/rate-limit error.
    """

    def __init__(
        self,
        openai_embeddings: OpenAIEmbeddings,
        local_embeddings: HuggingFaceEmbeddings,
    ):
        self._openai = openai_embeddings
        self._local = local_embeddings
        self._use_local = False

    def _switch_to_local(self) -> None:
        self._use_local = True

    def embed_query(self, text: str) -> List[float]:
        if self._use_local:
            return self._local.embed_query(text)

        try:
            return self._openai.embed_query(text)
        except Exception as e:
            if self._is_quota_error(e):
                self._switch_to_local()
                return self._local.embed_query(text)
            raise

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        if self._use_local:
            return self._local.embed_documents(texts)

        try:
            return self._openai.embed_documents(texts)
        except Exception as e:
            if self._is_quota_error(e):
                self._switch_to_local()
                return self._local.embed_documents(texts)
            raise

    def _is_quota_error(self, e: Exception) -> bool:
        err_msg = str(e).lower()
        err_type = str(type(e)).lower()
        return (
            "ratelimit" in err_type
            or "insufficient_quota" in err_msg
            or "429" in err_msg
        )


def get_embedding_model(fallback_to_local: Optional[bool] = None) -> Embeddings:
    """
    Returns an embedding model that:
      - Prefers OpenAI.
      - If USE_LOCAL_EMBEDDINGS=true in .env, always use local.
      - If OpenAI fails with quota/rate error, automatically falls back to local.
    """
    global _OPENAI_FALLBACK_TO_LOCAL

    # Environment flag takes precedence
    if _get_use_local_from_env():
        return _get_local_embeddings()

    if fallback_to_local is not None:
        _OPENAI_FALLBACK_TO_LOCAL = fallback_to_local

    if _OPENAI_FALLBACK_TO_LOCAL:
        return _get_local_embeddings()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        _OPENAI_FALLBACK_TO_LOCAL = True
        return _get_local_embeddings()

    openai_embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=api_key,
    )
    local_embeddings = _get_local_embeddings()

    return FallbackEmbeddings(openai_embeddings, local_embeddings)


def _get_local_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def set_openai_fallback_to_local(flag: bool) -> None:
    global _OPENAI_FALLBACK_TO_LOCAL
    _OPENAI_FALLBACK_TO_LOCAL = flag