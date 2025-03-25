from operator import truediv


def solve_maze(maze, start, end):
    stack = [start]
    visited = set()

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            print("출구 찾음", (x, y))
            return True

        if (x, y) not in visited:
            visited.add((x, y))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                    stack.append((nx, ny))

    print("출구를 찾을 수 없음")
    return False

maze = [
    [0,0,1,0,0],
    [1,0,1,0,1],
    [0,0,0,0,0],
    [1,1,0,1,0]
]

start = (0, 0)
end = (3, 4)

solve_maze(maze, start, end)