import re

def move(robot, direction, walls, boxes):
    boxes_to_move = boxes_infront(robot, direction, boxes)

    if move_boxes_infront(boxes_to_move, direction, walls, boxes):
        return move_robot(robot, direction, walls)
    return robot

def boxes_infront(robot, direction, boxes):
    res = list()
    x, y = robot
    dx, dy = direction
    x += dx
    y += dy

    while boxes[y][x]:
        res.append((x, y))
        x += dx
        y += dy

    return res

def move_boxes_infront(boxes_infront, direction, walls, boxes):
    if len(boxes_infront) == 0:
        return True
    
    dx, dy = direction

    first = boxes_infront[0]
    last = boxes_infront[-1]

    first_x, first_y = first
    last_x, last_y = last

    last_x += dx
    last_y += dy

    if not walls[last_y][last_x]:
        boxes[first_y][first_x] = False
        boxes[last_y][last_x] = True
        return True
    return False

def move_robot(robot, direction, walls):
    x, y = robot
    dx, dy = direction

    x += dx
    y += dy

    if walls[y][x]:
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

    ddic = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }

    walls = [[x == "#" for x in y] for y in m.split("\n")]
    boxes = [[x == "O" for x in y] for y in m.split("\n")]
    directions = [ddic[direction] for direction in d if direction != "\n"]
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

    # print(widen(m))

    # for y in range(len(walls)):
    #     r = ""
    #     for x in range(len(walls[0])):
    #         if (x, y) == robot:
    #             r += "@"
    #         # elif boxes[y][x]:
    #         #     r += "O"
    #         elif walls[y][x]:
    #             r += "#"
    #         else:
    #             r += "."
    #     print(r)

    # print(robot)

    for direction in directions:
        robot = move(robot, direction, walls, boxes)

    for y, l in enumerate(boxes):
        for x, c in enumerate(l):
            if c:
                part1 += y * 100 + x

    print("Part 1:", part1)
    print("Part 2:", part2)