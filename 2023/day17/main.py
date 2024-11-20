from collections import defaultdict
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
    
def add(queue, visited, cost, coordinate, direction, steps, heat_loss_map):
    x, y = coordinate
    dx, dy = direction
    new_x = x + dx
    new_y = y + dy
    if new_x < 0 or new_x >= len(heat_loss_map[0]) or new_y < 0 or new_y >= len(heat_loss_map):
        return
    to_add = (cost + heat_loss_map[new_y][new_x], (new_x, new_y), direction, steps + 1)
    if to_add[1:] in visited:
        return
    visited.add(to_add[1:])
    heappush(queue, to_add)

def dijkstra(start: tuple[int, int], min_steps: int, max_steps: int, heat_loss_map: list[list[int]]):
    # Coordinate, direction, current steps
    visited = set()
    
    # cost, coordinate, direction, steps
    queue = [(0, start, (1, 0), 0), (0, start, (0, 1), 0)]
    goal = (len(heat_loss_map[0]) - 1, len(heat_loss_map) - 1)
    current = queue[0] # temp

    while (current[3] < min_steps or current[1] != goal) and queue:
        current = heappop(queue)
        visited.add(current[1:])
        cost, coordinate, direction, steps = current

        if steps < max_steps:
            add(queue, visited, cost, coordinate, direction, steps, heat_loss_map)

        if steps >= min_steps:
            add(queue, visited, cost, coordinate, rotate(direction, True), 0, heat_loss_map)
            add(queue, visited, cost, coordinate, rotate(direction, False), 0, heat_loss_map)
    
    return current[0]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    heat_loss_map = list(list(int(y) for y in x) for x in data.splitlines())

    print("Part 1:", dijkstra((0, 0), 0, 3, heat_loss_map))
    print("Part 2:", dijkstra((0, 0), 4, 10, heat_loss_map))