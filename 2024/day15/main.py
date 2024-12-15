import re

def move(robot, direction, warehouse):
    boxes_to_move = get_boxes_infront(robot, direction, warehouse)

    if move_boxes(boxes_to_move, direction, warehouse):
        return move_robot(robot, direction, warehouse)
    return robot

def get_boxes_infront(robot, direction, warehouse):
    res = list()
    x, y = robot
    dx, dy = direction
    x += dx
    y += dy

    while warehouse[y][x] == "O":
        res.append((x, y))
        x += dx
        y += dy

    return res

def move_boxes(boxes, direction, warehouse):
    if len(boxes) == 0:
        return True
    
    dx, dy = direction

    first = boxes[0]
    last = boxes[-1]

    first_x, first_y = first
    last_x, last_y = last

    last_x += dx
    last_y += dy

    if warehouse[last_y][last_x] != "#":
        warehouse[first_y][first_x] = "."
        warehouse[last_y][last_x] = "O"
        return True
    return False

def move_robot(robot, direction, warehouse):
    x, y = robot
    dx, dy = direction

    x += dx
    y += dy

    if warehouse[y][x] == "#":
        return robot
    return (x, y)

def widen(m):
    res = re.subn(r"#", "##", m)[0]
    res = re.subn(r"O", "[]", res)[0]
    res = re.subn(r"\.", "..", res)[0]
    res = re.subn(r"@", "@.", res)[0]
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    m, d = data.split("\n\n")

    direction_dictionary = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }

    warehouse = [[x if x != "@" else "." for x in y] for y in m.split("\n")]

    directions = [direction_dictionary[direction] for direction in d if direction != "\n"]
    robot = (0, 0)

    for y, l in enumerate(m.split("\n")):
        for x, c in enumerate(l):
            if c == "@":
                robot = (x, y)
                break
        if robot != (0, 0):
            break

    part1 = 0
    part2 = 0

    for direction in directions:
        robot = move(robot, direction, warehouse)

    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == "O":
                part1 += y * 100 + x

    print("Part 1:", part1)
    print("Part 2:", part2)