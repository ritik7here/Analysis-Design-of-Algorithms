
from data import (
    parcels,
    graph,
    VEHICLE_CAPACITY,
    DEPOT
)

from algorithms.merge_sort import merge_sort
from algorithms.knapsack import knapsack

from algorithms.dijkstra import (
    dijkstra,
    reconstruct_path
)

from algorithms.tsp import nearest_neighbor_tsp


print("=" * 60)
print("INTELLIGENT COURIER PLANNING SYSTEM")
print("=" * 60)


# -----------------------------------------
# SORTING PARCELS
# -----------------------------------------

sorted_parcels = merge_sort(parcels)


# -----------------------------------------
# SELECTOMG PARCELS USING KNAPSACK
# -----------------------------------------

selected, max_value, dp_table = knapsack(
    sorted_parcels,
    VEHICLE_CAPACITY
)

print("\nSELECTED PARCELS")

for parcel in selected:
    print(
        parcel["parcel_id"],
        "| Destination:", parcel["destination"],
        "| Weight:", parcel["weight"],
        "| Value:", parcel["value"]
    )


# -----------------------------------------
# EXTRACTING UNIQUE DESTINATIONS
# -----------------------------------------

destinations = list(dict.fromkeys(
    parcel["destination"]
    for parcel in selected
))

print("\nUNIQUE DELIVERY DESTINATIONS:")
print(destinations)


# -----------------------------------------
# DIJKSTRA SHORTEST PATHS
# -----------------------------------------

print("\nINDIVIDUAL SHORTEST PATHS")
print("-" * 40)

for destination in destinations:

    distances, previous = dijkstra(
        graph,
        DEPOT
    )

    path = reconstruct_path(
        previous,
        DEPOT,
        destination
    )

    print(
        f"{DEPOT} -> {destination}: "
        f"{path} | Distance: {distances[destination]} km"
    )


# -----------------------------------------
# NEAREST NEIGHBOR TSP
# -----------------------------------------

print("\nOPTIMIZED DELIVERY ROUTE")
print("-" * 40)

route, total_distance = nearest_neighbor_tsp(
    graph,
    DEPOT,
    destinations
)

print("Route:", " -> ".join(route))

print("Total Route Distance:", total_distance, "km")


# -----------------------------------------
# FINAL DELIVERY SUMMARY
# -----------------------------------------

total_weight = sum(
    parcel["weight"]
    for parcel in selected
)

print("\nFINAL DELIVERY SUMMARY")
print("-" * 40)

print("Total Parcels:", len(selected))
print("Unique Destinations:", len(destinations))
print("Total Weight:", total_weight, "kg")
print("Vehicle Capacity:", VEHICLE_CAPACITY, "kg")
print("Total Parcel Value:", max_value)
print("Remaining Capacity:",
      VEHICLE_CAPACITY - total_weight, "kg")
print("Total Travel Distance:", total_distance, "km")

