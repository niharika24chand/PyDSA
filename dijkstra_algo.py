import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    dist = {}
    for i in graph:
        dist[i] = float('inf')
    dist[start] = 0

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_dist > dist[curr_node]:
            continue

        for n, w in graph[curr_node]:   #n=neighbor and w=weight
            new_dist = curr_dist + w
            if new_dist < dist[n]:
                dist[n] = new_dist
                heapq.heappush(queue, (new_dist, n))

    return dist

graph = {
    1 : [(2,7), (3, 9), (6, 14)],
    2 : [(1, 7), (3, 10), (4, 15)],
    3 : [(1, 9), (2, 10), (4, 11), (6, 2)],
    4 : [(2, 15), (3, 11), (5, 6)],
    5 : [(4, 6), (6, 9)],
    6 : [(1, 14), (3, 2), (5, 9)]
}
start = 1
s_paths = dijkstra(graph, start)
print(f"Shortest paths: {s_paths}")