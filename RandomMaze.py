import random

def generate_maze(width, height):
    # Initialize maze with walls
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Generate maze using depth-first search
    stack = [(0, 0)]
    while stack:
        x, y = stack[-1]
        maze[y][x] = 0  # Mark cell as part of the maze
        neighbors = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
        random.shuffle(neighbors)
        found = False
        for nx, ny in neighbors:
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[(ny + y) // 2][(nx + x) // 2] = 0  # Break the wall
                stack.append((nx, ny))
                found = True
                break
        if not found:
            stack.pop()

    return maze

def print_maze(maze):
    for row in maze:
        print("".join("██" if cell == 1 else "  " for cell in row))

# Example usage
maze_width = 21
maze_height = 21
maze = generate_maze(maze_width, maze_height)
print_maze(maze)
