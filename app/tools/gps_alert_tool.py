gps_alerts = {

    "V102": [
        "Overspeed alert",
        "Geofence exit alert"
    ],

    "V205": [
        "Maintenance overdue alert"
    ]
}

def get_vehicle_alerts(vehicle_id):

    return gps_alerts.get(

        vehicle_id,

        []
    )