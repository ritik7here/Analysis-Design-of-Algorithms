
from algorithms.dijkstra import dijkstra, reconstruct_path


def nearest_neighbor_tsp(graph, start, destinations):

    # Remove duplicate destinations and exclude warehouse
    destinations = list(dict.fromkeys(
        node for node in destinations if node != start
    ))

    unvisited = set(destinations)

    current = start

    route = [start]

    total_distance = 0

    # Build shortest-distance information for each node
    all_distances = {}
    all_previous = {}

    for node in graph:

        distances, previous = dijkstra(graph, node)

        all_distances[node] = distances
        all_previous[node] = previous

    # Visit nearest unvisited destination
    while unvisited:

        nearest = min(
            unvisited,
            key=lambda node: all_distances[current][node]
        )

        distance = all_distances[current][nearest]

        if distance == float("inf"):
            raise ValueError(
                f"No path from {current} to {nearest}"
            )

        total_distance += distance

        # Reconstruct actual road path
        segment = reconstruct_path(
            all_previous[current],
            current,
            nearest
        )

        route.extend(segment[1:])

        current = nearest

        unvisited.remove(nearest)

    # Return to warehouse
    return_distance = all_distances[current][start]

    if return_distance == float("inf"):
        raise ValueError("No return path to warehouse")

    return_segment = reconstruct_path(
        all_previous[current],
        current,
        start
    )

    route.extend(return_segment[1:])

    total_distance += return_distance

    return route, total_distance
