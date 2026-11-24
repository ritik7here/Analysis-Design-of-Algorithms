
from data import graph, parcels, VEHICLE_CAPACITY, DEPOT

from algorithms.merge_sort import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, reconstruct_path
from algorithms.tsp import nearest_neighbor_tsp


# Test 1: Merge Sort
sorted_parcels = merge_sort(parcels)

assert sorted_parcels == sorted(
    parcels,
    key=lambda p: (
        p["priority"],
        p["deadline"],
        p["parcel_id"]
    )
)

print("PASS: Merge Sort")


# Test 2: Knapsack
selected, value, dp = knapsack(
    sorted_parcels,
    VEHICLE_CAPACITY
)

total_weight = sum(p["weight"] for p in selected)

assert total_weight <= VEHICLE_CAPACITY

assert sum(p["value"] for p in selected) == value

print("PASS: Knapsack DP")


# Test 3: Dijkstra
distances, previous = dijkstra(graph, DEPOT)

assert distances["A"] == 4
assert distances["B"] == 6
assert distances["C"] == 9

path = reconstruct_path(previous, DEPOT, "C")

assert path[0] == DEPOT
assert path[-1] == "C"

print("PASS: Dijkstra")


# Test 4: Nearest Neighbor TSP
destinations = list(dict.fromkeys(
    p["destination"] for p in selected
))

route, distance = nearest_neighbor_tsp(
    graph,
    DEPOT,
    destinations
)

assert route[0] == DEPOT
assert route[-1] == DEPOT

assert set(destinations).issubset(set(route))

assert distance > 0

print("PASS: Nearest Neighbor TSP")


print("\nALL CORRECTNESS TESTS PASSED!")
