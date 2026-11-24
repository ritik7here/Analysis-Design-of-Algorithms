
# Parcel dataset for Intelligent Courier Planning System

parcels = [
    {
        "parcel_id": "P101",
        "destination": "A",
        "weight": 5,
        "priority": 1,
        "deadline": 10,
        "value": 100
    },
    {
        "parcel_id": "P102",
        "destination": "B",
        "weight": 8,
        "priority": 2,
        "deadline": 15,
        "value": 150
    },
    {
        "parcel_id": "P103",
        "destination": "C",
        "weight": 4,
        "priority": 1,
        "deadline": 8,
        "value": 120
    },
    {
        "parcel_id": "P104",
        "destination": "D",
        "weight": 10,
        "priority": 3,
        "deadline": 20,
        "value": 200
    },
    {
        "parcel_id": "P105",
        "destination": "E",
        "weight": 6,
        "priority": 2,
        "deadline": 12,
        "value": 130
    },
    {
        "parcel_id": "P106",
        "destination": "A",
        "weight": 3,
        "priority": 1,
        "deadline": 6,
        "value": 90
    }
]

# Vehicle maximum capacity in kg
VEHICLE_CAPACITY = 25

# Weighted delivery graph
graph = {
    "W": {"A": 4, "B": 6},
    "A": {"W": 4, "B": 2, "C": 5},
    "B": {"W": 6, "A": 2, "C": 3, "D": 7},
    "C": {"A": 5, "B": 3, "D": 4, "E": 6},
    "D": {"B": 7, "C": 4, "E": 2},
    "E": {"C": 6, "D": 2}
}

DEPOT = "W"
