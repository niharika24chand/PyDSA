#Ajacent list

graph = {
    'A' : ['C', 'D'],
    'B' : ['A', 'C'],
    'C' : ['D'],
    'D' : ['E']
}

print(graph)

#Adjacent matrix

graph = [
    [0, 1, 1, 0],  # Node A
    [1, 0, 0, 1],  # Node B
    [1, 0, 0, 1],  # Node C
    [0, 1, 1, 0]   # Node D
]

print(graph)