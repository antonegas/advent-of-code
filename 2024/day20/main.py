from collections import defaultdict
from itertools import combinations

def in_bound(width, height, coord):
    x, y = coord
    return x >= 0 and y >= 0 and x <= width and y <= height

def bfs(maze, start, end):
    queue = [start]
    explored = {start}
    previous = dict()
    steps_here = {start: 0}

    while len(queue) > 0:
        coord = queue.pop(0)
        if coord == end:
            return previous, steps_here
        x, y = coord
        for n in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            x2, y2 = n
            if n not in explored and in_bound(len(maze[0]), len(maze), coord) and maze[y2][x2] != "#":
                explored.add(n)
                previous[n] = coord
                steps_here[n] = steps_here[coord] + 1
                queue.append(n)

    return previous, steps_here

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    maze = [[x for x in y] for y in data.split("\n")]

    start = (0, 0)
    end = (0, 0)

    for y, l in enumerate(maze):
        for x, c in enumerate(l):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)

    part1 = 0
    part2 = 0

    previous, steps = bfs(maze, start, end)

    path = [end, previous[end]]

    while path[-1] != start:
        path.append(previous[path[-1]])

    cheats = defaultdict(lambda: 0)

    for tile2, tile1 in combinations(path, 2):
        x1, y1 = tile1
        x2, y2 = tile2
        diff = abs(x1 - x2) + abs(y1 - y2)
        if diff >= 2 and diff <= 2:
            save = steps[tile2] - steps[tile1] - diff
            if save >= 100:
                if diff == 2:
                    part1 += 1
                part2 += 1

    print("Part 1:", part1)
    print("Part 2:", part2)