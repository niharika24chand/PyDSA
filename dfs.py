def DFS(graph, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for i in graph[node]:
        if i not in visited:
            DFS(graph, i, visited)


graph = {
    1 : [2,3],
    2 : [4,5],
    3 : [6],
    4 : [],
    5 : [],
    6: []
}

print("DFS traversal starting from node 1:")
DFS(graph, 1)