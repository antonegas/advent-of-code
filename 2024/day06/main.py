def in_bound(patrol_map, position):
    x, y = position
    return x >= 0 and y >= 0 and x < len(patrol_map[0]) and y < len(patrol_map)

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    patrol_map = [x for x in data.split("\n")]

    part1 = 0
    part2 = 0

    initial_dx = 0
    initial_dy = 0
    start = (0, 0,)

    for x in range(len(patrol_map[0])):
        for y in range(len(patrol_map)):
            if patrol_map[y][x] == "^":
                initial_dy = -1
                start = (x, y,)
                break
            if patrol_map[y][x] == "v":
                initial_dy = 1
                start = (x, y,)
                break
            if patrol_map[y][x] == "<":
                initial_dx = -1
                start = (x, y,)
                break
            if patrol_map[y][x] == ">":
                initial_dx = 1
                start = (x, y,)
                break

    dx = initial_dx
    dy = initial_dy

    positions = set()
    current_position = start

    while True:
        x, y = current_position
        moved_position = (x + dx, y + dy)

        if not in_bound(patrol_map, moved_position):
            break

        if patrol_map[moved_position[1]][moved_position[0]] == "#":
            if dy == -1:
                dx = 1
                dy = 0
            elif dx == 1:
                dx = 0
                dy = 1
            elif dy == 1:
                dx = -1
                dy = 0
            elif dx == -1:
                dx = 0
                dy = -1
        else:
            current_position = moved_position
            positions.add(current_position)

    obstructions = set()

    for position in positions:
        if position == start:
            continue

        obstruction = position
        visited = set()
        
        dx = initial_dx
        dy = initial_dy

        current_position = start

        while True:
            if (*current_position, dx, dy) in visited:
                obstructions.add(obstruction)
                break

            visited.add((*current_position, dx, dy))

            x, y = current_position
            moved_position = (x + dx, y + dy)

            if not in_bound(patrol_map, moved_position):
                break

            if moved_position == obstruction or patrol_map[moved_position[1]][moved_position[0]] == "#":
                if dy == -1:
                    dx = 1
                    dy = 0
                elif dx == 1:
                    dx = 0
                    dy = 1
                elif dy == 1:
                    dx = -1
                    dy = 0
                elif dx == -1:
                    dx = 0
                    dy = -1
            else:
                current_position = moved_position


    print("Part 1:", len(positions))
    print("Part 2:", len(obstructions))

