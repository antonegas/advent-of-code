from functools import reduce
import re
from math import floor, ceil, gcd
from statistics import variance

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

def position_after_nseconds(width, height, robot, n):
    return x_after_nseconds(width, robot, n), y_after_nseconds(height, robot, n)

def x_after_nseconds(width, robot, n):
    p, v = robot
    x0, _ = p
    dx, _ = v
    return (x0 + dx * n) % width

def y_after_nseconds(height, robot, n):
    p, v = robot
    _, y0 = p
    _, dy = v
    return (y0 + dy * n) % height

def modular_inverse(a, m):
    # ax = 1 mod m
    assert gcd(a, m) == 1
    return pow(a, -1, m) # Can't be math.pow()

def save_tree_image(width, height, robots, tree_time):
    tree_robots = {position_after_nseconds(width, height, robot, tree_time) for robot in robots}
    bitmap_lines = list(map(" ".join, [["1" if (x, y) in tree_robots else "0" for x in range(width)] for y in range(height)]))
    with open(os.path.join(__location__, "tree.pgm"), 'w') as f:
        f.write("\n".join(["P1", f"{width} {height}"] + bitmap_lines))
        f.close()

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
        x100, y100 = position_after_nseconds(WIDTH, HEIGHT, robot, SECONDS)
        quadrant = get_quadrant(WIDTH, HEIGHT, x100, y100)
        if quadrant >= 0:
            quadrants[quadrant] += 1

    different_positions = set()

    best_x_variance = float('inf')
    best_y_variance = float('inf')
    best_x = 0
    best_y = 0

    for n in range(1, max(WIDTH, HEIGHT) + 1):
        x_variance = variance([x_after_nseconds(WIDTH, robot, n) for robot in robots])
        y_variance = variance([y_after_nseconds(HEIGHT, robot, n) for robot in robots])
        if x_variance < best_x_variance:
            best_x_variance = x_variance
            best_x = n
        if y_variance < best_y_variance:
            best_y_variance = y_variance
            best_y = n
    
    # Chinese remainder
    part2 = (best_x + modular_inverse(WIDTH, HEIGHT) * (best_y - best_x) * WIDTH) % (WIDTH * HEIGHT)

    print("Part 1:", reduce(lambda x, y: x * y, quadrants))
    print("Part 2:", part2)
    # save_tree_image(WIDTH, HEIGHT, robots, part2)