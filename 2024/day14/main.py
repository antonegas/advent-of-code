from functools import reduce
import re
from math import floor, ceil

def get_quadrant(width, height, x, y):
    if x >= 0 and x < floor(width / 2):
        if y >= 0 and y < floor(height / 2):
            return 0
        elif y < height and y >= ceil(height / 2):
            return 2
    elif x < width and x >= ceil(width / 2):
        if y >= 0 and y < floor(height / 2):
            return 1
        elif y < height and y >= ceil(height / 2):
            return 3
    return -1

def position_in_nseconds(width, height, robot, n):
    p, v = robot
    x0, y0 = p
    dx, dy = v
    xn = (x0 + dx * n) % width
    yn = (y0 + dy * n) % height
    return xn, yn

def save_tree_image(width, height, robot_positions):
    try:
        import png # pip install pypng
    except:
        return
    
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for position in robot_positions:
        x, y = position
        grid[y][x] += 1

    tree = list()

    for y in grid:
        r = list()
        for x in y:
            if x > 0:
                r.append(1)
            else:
                r.append(0)
        tree.append(r)
    
    writer = png.Writer(width=width, height=height, bitdepth=1)

    with open(os.path.join(__location__, "tree.png"), 'wb') as f:
        writer.write(f, tree)

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    robots = [[list(map(int, re.findall(r"-?\d+", y))) for y in x.split(" ")] for x in data.split("\n")]

    WIDTH = 101
    HEIGHT = 103
    SECONDS = 100

    part2 = 0

    quadrants = [0 for _ in range(4)]

    for robot in robots:
        x100, y100 = position_in_nseconds(WIDTH, HEIGHT, robot, SECONDS)
        quadrant = get_quadrant(WIDTH, HEIGHT, x100, y100)
        if quadrant >= 0:
            quadrants[quadrant] += 1

    different_positions = set()

    while len(different_positions) != len(robots):
        part2 += 1
        different_positions = set()
        for robot in robots:
            different_positions.add(position_in_nseconds(WIDTH, HEIGHT, robot, part2))

    print("Part 1:", reduce(lambda x, y: x * y, quadrants))
    print("Part 2:", part2)
    save_tree_image(WIDTH, HEIGHT, different_positions)