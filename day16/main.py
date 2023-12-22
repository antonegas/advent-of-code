UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def beam(contraption, start, direction):
    energized = dict()
    # coordinate, (dx, dy)
    stack: list[tuple[tuple[int, int], tuple[int, int]]] = list()
    stack.append((start, direction))

    while len(stack) > 0:
        coordinate, deltas = stack.pop(0)
        x, y = coordinate
        if (coordinate in energized and deltas in energized[coordinate]) or x < 0 or x >= len(contraption[0]) or y < 0 or y >= len(contraption):
            continue
        elif coordinate in energized:
            energized[coordinate].add(deltas)
        else:
            energized[coordinate] = {deltas}

        stack.extend(move_beam(contraption, coordinate, deltas))

    return energized

def move_beam(contraption, coordinate, deltas):
    x, y = coordinate 
    to_add: list[tuple[tuple[int, int], tuple[int, int]]] = list()

    if contraption[y][x] == "-" and (deltas == UP or deltas == DOWN):
        to_add.append(((x - 1, y), LEFT))
        to_add.append(((x + 1, y), RIGHT))
    elif contraption[y][x] == "|" and (deltas == LEFT or deltas == RIGHT):
        to_add.append(((x, y - 1), UP))
        to_add.append(((x, y + 1), DOWN))
    elif contraption[y][x] == "\\":
        if deltas == UP:
            to_add.append(((x - 1, y), LEFT))
        elif deltas == DOWN:
            to_add.append(((x + 1, y), RIGHT))
        elif deltas == LEFT:
            to_add.append(((x, y - 1), UP))
        else: # RIGHT
            to_add.append(((x, y + 1), DOWN))
    elif contraption[y][x] == "/":
        if deltas == UP:
            to_add.append(((x + 1, y), RIGHT))
        elif deltas == DOWN:
            to_add.append(((x - 1, y), LEFT))
        elif deltas == LEFT:
            to_add.append(((x, y + 1), DOWN))
        else: # RIGHT
            to_add.append(((x, y - 1), UP))
    else: # "."
        dx, dy = deltas
        to_add.append(((x + dx, y + dy), deltas))

    return to_add

def edge_generator(contraption):
    x_bound = len(contraption[0])
    y_bound = len(contraption)

    for x in range(x_bound):
        yield (x, 0), DOWN
        yield (x, y_bound - 1), UP

    for y in range(y_bound):
        yield (0, y), RIGHT
        yield (x_bound - 1, y), LEFT

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    contraption = list(list(x) for x in data.split("\n"))

    print("Part 1:", len([x for x in beam(contraption, (0, 0), RIGHT)]))
    print("Part 2:", max([len([x for x in beam(contraption, coordinate, direction)]) for coordinate, direction in edge_generator(contraption)]))
    