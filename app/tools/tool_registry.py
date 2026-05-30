from app.tools.vehicle_lookup_tool import (
    vehicle_lookup
)

from app.tools.maintenance_tool import (
    get_maintenance_status
)

from app.tools.gps_alert_tool import (
    get_vehicle_alerts
)

tool_registry = {

    "vehicle_lookup": vehicle_lookup,

    "maintenance_status": (
        get_maintenance_status
    ),

    "gps_alerts": get_vehicle_alerts
}