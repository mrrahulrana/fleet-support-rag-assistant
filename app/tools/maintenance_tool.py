maintenance_data = {

    "V102": {
        "maintenance_due": "2026-06-15",
        "odometer": 145230,
        "status": "Due in 1200 km"
    },

    "V205": {
        "maintenance_due": "2026-05-30",
        "odometer": 201540,
        "status": "Overdue"
    }
}

def get_maintenance_status(vehicle_id):

    return maintenance_data.get(

        vehicle_id,

        {
            "error": "Maintenance data unavailable"
        }
    )