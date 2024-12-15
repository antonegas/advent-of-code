import re

def move(robot, direction, warehouse):
    boxes_to_move = boxes_blocking(robot, direction, warehouse)

    if move_boxes(boxes_to_move, direction, warehouse):
        return move_robot(robot, direction, warehouse)
    return robot

def move_wide(robot, direction, wide_warehouse):
    dx, dy = direction

    if dx != 0:
        boxes_to_move = wide_blocking_x(robot, dx, wide_warehouse)
        if move_wide_x(boxes_to_move, dx, wide_warehouse):
            return move_robot(robot, direction, wide_warehouse)
    elif dy != 0:
        boxes_to_move = wide_blocking_y(robot, dy, wide_warehouse)
        if move_wide_y(boxes_to_move, dy, wide_warehouse):
            return move_robot(robot, direction, wide_warehouse)
    return robot

def boxes_blocking(robot, direction, warehouse):
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

def wide_blocking_x(robot, dx, wide_warehouse):
    wide_box_side = "[" if dx > 0 else "]"
    
    res = list()
    x, y = robot
    x += dx

    while wide_warehouse[y][x] == wide_box_side:
        res.append((x, y))
        x += dx * 2

    return res

def wide_blocking_y(robot, dy, wide_warehouse):
    res = list()
    x, y = robot
    y += dy

    if wide_warehouse[y][x] in "[]":
        res.append({with_leftmost_x(x, y, wide_warehouse)})
    else:
        return res

    while len(res[-1]) > 0:
        y += dy
        res.append(set())
        for x, _ in res[-2]:
            for i in range(2):
                if wide_warehouse[y][x + i] in "[]":
                    res[-1].add(with_leftmost_x(x + i, y, wide_warehouse))

    # Flattened res
    return [box for boxes in res for box in boxes]

def with_leftmost_x(x, y, wide_warehouse):
    if wide_warehouse[y][x] == "[":
        return (x, y)
    return (x - 1, y)

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

def move_wide_x(wide_boxes, dx, wide_warehouse):
    if len(wide_boxes) == 0:
        return True
    
    wide_box_sides = "[]" if dx > 0 else "]["
    
    last = wide_boxes[-1]
    last_x, y = last
    last_x += dx * 2

    if wide_warehouse[y][last_x] != "#":
        for x, _ in wide_boxes:
            wide_warehouse[y][x] = "."
            wide_warehouse[y][x + 1] = "."
        for x, _ in wide_boxes:
            wide_warehouse[y][x + dx] = wide_box_sides[0]
            wide_warehouse[y][x + dx * 2] = wide_box_sides[1]
        return True
    return False

def move_wide_y(wide_boxes, dy, wide_warehouse):
    if len(wide_boxes) == 0:
        return True
    
    if all(["#" not in wide_warehouse[y + dy][x] + wide_warehouse[y + dy][x + 1] for x, y in wide_boxes]): 
        for x, y in reversed(wide_boxes):
            wide_warehouse[y][x] = "."
            wide_warehouse[y][x + 1] = "."
            wide_warehouse[y + dy][x] = "["
            wide_warehouse[y + dy][x + 1] = "]"
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
    raw_warehouse, raw_directions = data.split("\n\n")

    direction_dictionary = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }

    warehouse = [[x if x != "@" else "." for x in y] for y in raw_warehouse.split("\n")]
    wide_warehouse = [[x if x != "@" else "." for x in y] for y in widen(raw_warehouse).split("\n")]

    directions = [direction_dictionary[direction] for direction in raw_directions if direction != "\n"]
    
    robot1 = (0, 0)
    robot2 = (0, 0)

    for y, l in enumerate(raw_warehouse.split("\n")):
        for x, c in enumerate(l):
            if c == "@":
                robot1 = (x, y)
                break
        if robot1 != (0, 0):
            break

    for y, l in enumerate(widen(raw_warehouse).split("\n")):
        for x, c in enumerate(l):
            if c == "@":
                robot2 = (x, y)
                break
        if robot2 != (0, 0):
            break

    part1 = 0
    part2 = 0

    for i, direction in enumerate(directions):
        robot1 = move(robot1, direction, warehouse)
        robot2 = move_wide(robot2, direction, wide_warehouse)

    for y, l in enumerate(warehouse):
        for x, c in enumerate(l):
            if c == "O":
                part1 += y * 100 + x

    for y, l in enumerate(wide_warehouse):
        for x, c in enumerate(l):
            if c == "[":
                part2 += y * 100 + x

    print("Part 1:", part1)
    print("Part 2:", part2)