#To find a path from a starting position to an ending position in a maze using Depth-First Search (Example for backtracking)
def solve_maze(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        curr_pos, path = stack.pop()
        if curr_pos == end:
            return path
        visited.add(curr_pos)

        for move in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
            if new_pos not in visited and is_valid_move(maze, new_pos):
                stack.append((new_pos, path+[new_pos]))
    return None

def is_valid_move(maze, pos):
    x, y = pos
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

maze =[
    [0,1,0,0],
    [0,1,0,1],
    [0,0,0,1],
    [1,1,0,0]
]

start = (0,0)
end = (3,3)
path= solve_maze(maze, start, end)
print("Path to exit: ",path)