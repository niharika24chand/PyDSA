import heapq  # Used to implement a priority queue (min-heap) for efficiently retrieving the node with the smallest distance.

def dijkstra(graph, start):
    # Priority queue (min-heap)
    queue = [(0, start)]
    distances = {}
    # Initialize distances
    for i in graph:
        distances[i] = float('inf')
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)  #heapq.heappop(queue) retrieves and removes the node with the smallest distance (current_distance) from the queue.

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors (directly iterate over list of tuples)
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}

start_node = 1
shortest_path = dijkstra(graph, start_node)
print(shortest_path)
