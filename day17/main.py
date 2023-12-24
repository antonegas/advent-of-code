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
    
def neighbors(node, max_repeat, heat_loss_map):
    coordinate, direction, repeat = node
    new_repeat = repeat + 1
    x, y = coordinate
    possible_neighbors = list()
    # Go forward
    if new_repeat < max_repeat:
        dx, dy = direction
        possible_neighbors.append(((x + dx, y + dy), direction, new_repeat))
    # rotate left
    left_direction = rotate(direction, False)
    left_dx, left_dy = left_direction
    possible_neighbors.append(((x + left_dx, y + left_dy), left_direction, 0))
    # rotate right
    right_direction = rotate(direction, True)
    right_dx, right_dy = right_direction
    possible_neighbors.append(((x + right_dx, y + right_dy), right_direction, 0))

    res = list()

    for possible_neighbor in possible_neighbors:
        coordinate, _, _ = possible_neighbor
        x, y = coordinate
        if x >= 0 and x < len(heat_loss_map[0]) and y >= 0 and y < len(heat_loss_map):
            res.append(possible_neighbor)

    return res

def path_from_previous(start, goal_key, previous):
    path = [goal_key[0]]
    current = goal_key
    while current[0] != start:
        current = previous[current]
        path.append(current[0])
    return list(reversed(path))

def total_heat_loss(path, heat_loss_map):
    total = 0
    for node in path[1:]:
        x, y = node
        total += heat_loss_map[y][x]
    return total

def dijkstra(start: tuple[int, int], direction: tuple[int, int], max_repeat: int, heat_loss_map: list[list[int]]):
    # Coordinate, direction, current repeat: cost
    visited = set()
    costs: dict[tuple[tuple[int, int], tuple[int, int], int], int] = dict()
    previous: dict[tuple[tuple[int, int], tuple[int, int], int], tuple[int, int]] = dict()

    for i in range(max_repeat):
        for _direction in DIRECTIONS:
            costs[(start, _direction, i)] = 0
    
    queue = [(start, direction, 0)]
    goal = (len(heat_loss_map[0]) - 1, len(heat_loss_map) - 1)
    current = [0] # temp

    while current[0] != goal and queue:
        queue.sort(key=lambda x: costs[x])
        current = queue.pop(0)
        visited.add(current)

        for neighbor in neighbors(current, max_repeat, heat_loss_map):
            if neighbor in visited or neighbor in queue:
                continue
            else:
                queue.append(neighbor)
            cost_to_neighbor = heat_loss_map[neighbor[0][1]][neighbor[0][0]]
            if neighbor not in costs:
                costs[neighbor] = float("inf")
            other_cost = costs[current] + cost_to_neighbor
            if other_cost < costs[neighbor]:
                costs[neighbor] = other_cost
                previous[neighbor] = current

    return current, previous

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    heat_loss_map = list(list(int(y) for y in x) for x in data.splitlines())


    print("Part 1:", total_heat_loss(path_from_previous((0, 0), *dijkstra((0, 0), RIGHT, 3, heat_loss_map)), heat_loss_map))
    print("Part 2:", 0)