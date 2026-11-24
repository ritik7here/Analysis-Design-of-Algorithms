
import heapq


def dijkstra(graph, start):

    # Initialize distances
    distances = {
        node: float("inf")
        for node in graph
    }

    # Store previous nodes for path reconstruction
    previous = {
        node: None
        for node in graph
    }

    distances[start] = 0

    # Priority queue: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        # Ignore outdated queue entries
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, previous


def reconstruct_path(previous, start, destination):

    path = []
    current = destination

    while current is not None:

        path.append(current)

        if current == start:
            break

        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path
