# Intelligent Courier Planning and Optimization System

## 1. Project Overview

The Intelligent Courier Planning and Optimization System is a Python-based prototype designed to simulate an intelligent courier delivery service.

The system selects parcels based on vehicle capacity, prioritizes deliveries, calculates shortest paths between locations, and generates an approximate optimized delivery route.

It integrates sorting algorithms, dynamic programming, graph algorithms, and approximation techniques.

## 2. Objectives

- Prioritize parcels according to delivery priority and deadlines.
- Select the most valuable combination of parcels within vehicle capacity.
- Find shortest paths between delivery locations.
- Generate an approximate delivery route.
- Analyze algorithm execution time for different input sizes.

## 3. Technologies Used

- Programming Language: Python
- Libraries: Matplotlib, Random, Time, Heapq, CSV
- Development Environment: Visual Studio Code
- Data Structures: Lists, Dictionaries, Graphs, DP Tables, Priority Queues

## 4. Algorithms Implemented

### Merge Sort
Sorts parcels by priority, deadline, and parcel ID.

Time Complexity: O(n log n)

Space Complexity: O(n)

### 0/1 Knapsack using Dynamic Programming
Selects parcels to maximize total parcel value without exceeding vehicle capacity.

Time Complexity: O(nW)

Space Complexity: O(nW)

### Dijkstra's Algorithm
Calculates shortest paths between delivery locations using a weighted graph.

Time Complexity: O((V + E) log V)

Space Complexity: O(V + E)

### Nearest Neighbor TSP Approximation
Generates an approximate delivery route by repeatedly visiting the nearest unvisited destination.

In this implementation, shortest road distances are calculated using Dijkstra's algorithm.

Preprocessing Complexity: O(V(V + E) log V)

Additional route-selection complexity: O(V²)

## 5. Project Structure

```text
intelligent-courier-system/
├── main.py
├── data.py
├── algorithms/
│   ├── merge_sort.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
├── analysis/
│   ├── performance.py
│   └── test_performance.py
├── results/
├── screenshots/
└── README.md
```

## 6. Installation and Execution

Install the required dependency:

```bash
pip install matplotlib
```

Run the main application:

```bash
python main.py
```

Run performance analysis:

```bash
python -m analysis.performance
```

Run correctness tests:

```bash
python -m analysis.test_performance
```

## 7. Performance Analysis

The system evaluates algorithm execution time using different parcel counts and graph sizes.

Parcel dataset sizes:
- 10
- 50
- 100
- 200
- 500

Graph sizes:
- 10
- 20
- 40
- 60
- 80

The benchmark results are stored in CSV format, and performance graphs are generated using Matplotlib.

Actual measured results are available in `results/performance_results.csv`.

## 8. Results

The system successfully demonstrates:
- Parcel prioritization using Merge Sort.
- Optimal parcel selection using 0/1 Knapsack DP.
- Shortest-path calculation using Dijkstra's algorithm.
- Approximate route generation using Nearest Neighbor TSP.
- Performance measurement and visualization.

## 9. Limitations

- The road network uses simulated distances.
- Nearest Neighbor does not guarantee the globally optimal TSP route.
- The system assumes a single delivery vehicle.
- Delivery deadlines are used for parcel prioritization but are not explicitly enforced as time-window constraints.
- Vehicle loading and unloading time is not considered.

## 10. Conclusion

The Intelligent Courier Planning and Optimization System demonstrates how fundamental data structures and algorithms can be combined to solve a practical logistics problem.

The project integrates sorting, dynamic programming, shortest-path algorithms, and approximation techniques into a unified courier planning prototype.

It also demonstrates the importance of performance analysis when evaluating algorithms on increasing input sizes.
