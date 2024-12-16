from heapq import heappush, heappop

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def rotate(direction: tuple[int, int], clockwise: bool):
    dx, dy = direction
    if clockwise:
        return (-dy, dx)
    else:
        return (dy, -dx)
    
def move(direction: tuple[int, int], coordinate: tuple[int, int]):
    dx, dy = direction
    x, y = coordinate
    return (x + dx, y + dy)
    
def add1(queue, visited, cost, coordinate, direction, maze):
    x, y = coordinate
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return
    if maze[y][x] == "#":
        return
    state = (coordinate, direction)
    if state in visited:
        return
    visited.add(state)
    to_add = (cost, coordinate, direction)
    heappush(queue, to_add)

def add2(queue, visited, cost, coordinate, direction, path, maze):
    x, y = coordinate
    if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
        return
    if maze[y][x] == "#":
        return
    state = (coordinate, direction)
    if state in visited:
        return
    to_add = (cost, coordinate, direction, path)
    heappush(queue, to_add)

def dijkstra1(start: tuple[int, int], end: tuple[int, int], maze: list[list[str]]):
    # cost, coordinate, direction
    queue = [(0, start, RIGHT)]
    current = queue[0] # temp
    visited = set()

    while (current[1] != end) and queue:
        current = heappop(queue)
        visited.add(current[1:])
        cost, coordinate, direction = current

        add1(queue, visited, cost + 1, move(direction, coordinate), direction, maze)
        add1(queue, visited, cost + 1000, coordinate, rotate(direction, True), maze)
        add1(queue, visited, cost + 1000, coordinate, rotate(direction, False), maze)
    
    return current[0]

def dijkstra2(best_cost: int, start: tuple[int, int], end: tuple[int, int], maze: list[list[str]]):
    # Coordinate, direction
    
    # cost, coordinate, direction
    queue = [(0, start, RIGHT, [start])]
    current = queue[0] # temp
    visited = set()

    path_tiles = set()

    while queue:
        current = heappop(queue)
        cost, coordinate, direction, path = current
        visited.add((coordinate, direction))

        if cost > best_cost:
            break
        if current[1] == end:
            path_tiles.update(set(path))

        moved = move(direction, coordinate)
        direction2 = rotate(direction, True)
        moved2 = move(direction2, coordinate)
        direction3 = rotate(direction, False)
        moved3 = move(direction3, coordinate)

        add2(queue, visited, cost + 1, moved, direction, path + [moved], maze)
        add2(queue, visited, cost + 1000, moved2, direction2, path + [moved2], maze)
        add2(queue, visited, cost + 1000, moved3, direction3, path + [moved3], maze)
    
    return path_tiles

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    maze = [[x for x in y] for y in data.split("\n")]

    start = (0, 0)
    end = (0, 0)

    for y, l in enumerate(maze):
        for x, c in enumerate(l):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif start != (0, 0) and end != (0, 0):
                break
        if start != (0, 0) and end != (0, 0):
            break

    part1 = 0
    part2 = 0

    part1 = dijkstra1(start, end, maze)
    part2 = len(dijkstra2(part1, start, end, maze))

    print("Part 1:", part1)
    print("Part 2:", part2)