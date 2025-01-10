def find_start(patrol_map):
    for x in range(len(patrol_map[0])):
        for y in range(len(patrol_map)):
            if patrol_map[y][x] == "^":
                return x, y

    return -1, -1

def in_bound(patrol_map, x, y):
    return x >= 0 and y >= 0 and x < len(patrol_map[0]) and y < len(patrol_map)

def patrol(patrol_map, start):
    x, y = start
    dx, dy = 0, -1

    positions = set()
    visited = set()

    while True:
        if (x, y, dx, dy) in visited:
            return positions, True
        
        visited.add((x, y, dx , dy))

        next_x = x + dx
        next_y = y + dy

        if not in_bound(patrol_map, next_x, next_y):
            return positions, False

        if patrol_map[next_y][next_x] == "#":
            dx, dy = -dy, dx
        else:
            x, y = next_x, next_y
            positions.add((x, y))

def get_infinite_obstructions(patrol_map, positions, start):
    obstructions = set()

    for position in positions:
        if position == start:
            continue

        x, y = position
        patrol_map[y][x] = "#"

        _, infinite = patrol(patrol_map, start)
        if infinite:
            obstructions.add((x, y))

        patrol_map[y][x] = "."

    return obstructions

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    patrol_map = [[x for x in y] for y in data.split("\n")]

    start = find_start(patrol_map)
    positions, _ = patrol(patrol_map, start)
    obstructions = get_infinite_obstructions(patrol_map, positions, start)

    print("Part 1:", len(positions))
    print("Part 2:", len(obstructions))