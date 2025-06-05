from collections import deque
def BFS(graph, root):
    visited = set()
    for node in graph:  
        if node not in visited:
            queue = deque([node])
            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    for i in graph[vertex]:
                        if i not in visited:
                            queue.append(i)

    print(visited)

if __name__ == "__main__":
    graph = {
        0 : [1,2,3],
        1 : [0,2],
        2 : [0,1],
        3 : [0],
        4 : [2]
    }
    BFS(graph, 0)
    