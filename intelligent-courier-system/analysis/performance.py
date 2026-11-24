import time
import random
import csv
import os
import matplotlib.pyplot as plt

from algorithms.merge_sort import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp


# -----------------------------------------
# RANDOM PARCEL DATA
# -----------------------------------------

def generate_parcels(n):

    parcels = []

    for i in range(n):

        parcels.append({
            "parcel_id": f"P{i}",
            "destination": "W",
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 5),
            "deadline": random.randint(1, 100),
            "value": random.randint(50, 500)
        })

    return parcels


# -----------------------------------------
# CONNECTED GRAPh
# -----------------------------------------

def generate_graph(n):

    graph = {
        str(i): {}
        for i in range(n)
    }

    # Connect consecutive nodes
    for i in range(n - 1):

        weight = random.randint(1, 20)

        graph[str(i)][str(i + 1)] = weight
        graph[str(i + 1)][str(i)] = weight

    # Add random edges
    for i in range(n):

        for j in range(i + 2, n):

            if random.random() < 0.15:

                weight = random.randint(1, 20)

                graph[str(i)][str(j)] = weight
                graph[str(j)][str(i)] = weight

    return graph


# -----------------------------------------
# MEz. Execution Time
# -----------------------------------------

def measure_time(function, *args, repeats=3):

    times = []

    for _ in range(repeats):

        start = time.perf_counter()

        function(*args)

        end = time.perf_counter()

        times.append(end - start)

    return sum(times) / len(times)


# -----------------------------------------
# algo benchmark
# -----------------------------------------

def benchmark():

    parcel_sizes = [10, 50, 100, 200, 500]

    graph_sizes = [10, 20, 40, 60, 80]

    results = []

    print("\nPERFORMANCE BENCHMARK")
    print("=" * 65)

    # Parcel algorithm benchmarks
    for size in parcel_sizes:

        parcels = generate_parcels(size)

        sorting_time = measure_time(
            merge_sort, parcels
        )

        knapsack_time = measure_time(
            knapsack, parcels, 25
        )

        results.append({
            "algorithm": "Merge Sort",
            "input_size": size,
            "time_seconds": sorting_time
        })

        results.append({
            "algorithm": "Knapsack DP",
            "input_size": size,
            "time_seconds": knapsack_time
        })

        print(
            f"Parcels: {size:3d} | "
            f"Merge Sort: {sorting_time:.8f}s | "
            f"Knapsack: {knapsack_time:.8f}s"
        )

    # Graph algorithm benchmarks
    for size in graph_sizes:

        graph = generate_graph(size)

        start_node = "0"

        dijkstra_time = measure_time(
            dijkstra, graph, start_node
        )

        destinations = [
            str(i)
            for i in range(1, size)
        ]

        tsp_time = measure_time(
            nearest_neighbor_tsp,
            graph,
            start_node,
            destinations,
            repeats=1
        )

        results.append({
            "algorithm": "Dijkstra",
            "input_size": size,
            "time_seconds": dijkstra_time
        })

        results.append({
            "algorithm": "Nearest Neighbor TSP",
            "input_size": size,
            "time_seconds": tsp_time
        })

        print(
            f"Graph Nodes: {size:3d} | "
            f"Dijkstra: {dijkstra_time:.8f}s | "
            f"TSP: {tsp_time:.8f}s"
        )

    return results


# -----------------------------------------
# SAVING RESULTS TO CSV
# -----------------------------------------

def save_results(results):

    os.makedirs("results", exist_ok=True)

    with open(
        "results/performance_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "algorithm",
                "input_size",
                "time_seconds"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nResults saved successfully!")


# -----------------------------------------
# PERFORMANCE GRAPHS
# -----------------------------------------

def plot_results(results):

    algorithms = [
        "Merge Sort",
        "Knapsack DP",
        "Dijkstra",
        "Nearest Neighbor TSP"
    ]

    os.makedirs("results", exist_ok=True)

    for algorithm in algorithms:

        data = [
            item for item in results
            if item["algorithm"] == algorithm
        ]

        sizes = [
            item["input_size"]
            for item in data
        ]

        times = [
            item["time_seconds"]
            for item in data
        ]

        plt.figure()

        plt.plot(
            sizes,
            times,
            marker="o",
            label=algorithm
        )

        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")

        plt.title(
            f"Performance Analysis - {algorithm}"
        )

        plt.legend()
        plt.grid(True)

        filename = algorithm.lower().replace(" ", "_")

        plt.savefig(
            f"results/{filename}_performance.png"
        )

        plt.close()



if __name__ == "__main__":

    results = benchmark()

    save_results(results)

    plot_results(results)

    print("\nAll performance tests completed!")
