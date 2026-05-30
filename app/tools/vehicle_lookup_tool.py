mock_vehicle_data = {

    "V102": {
        "status": "Active",
        "driver": "Michael Weber",
        "last_location": "Frankfurt",
        "speed": 92
    },

    "V205": {
        "status": "Maintenance",
        "driver": "Anna Schmidt",
        "last_location": "Munich",
        "speed": 0
    }
}

def vehicle_lookup(vehicle_id):

    return mock_vehicle_data.get(

        vehicle_id,

        {
            "error": "Vehicle not found"
        }
    )