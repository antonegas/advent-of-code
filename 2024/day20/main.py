from collections import defaultdict


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

    previous, steps_there = bfs(maze, start, end)

    path = [end, previous[end]]

    while path[-1] != start:
        path.append(previous[path[-1]])
        # print(steps_there[path[-1]])

    # for y, l in enumerate(maze):
    #     r = ""
    #     for x, c in enumerate(l):
    #         if (x, y) in path:
    #             r += "O"
    #         else:
    #             r += c
    #     print(r)

    cheats = defaultdict(lambda: 0)

    for tile in path:
        x, y = tile
        for n in [(0, - 1), (0, 1), (-1, 0), (1, 0)]:
            dx, dy = n
            if in_bound(len(maze), len(maze[0]), (x + dx, y + dy)) and maze[y + dy][x + dx] == "#":
                cheated_position = (x + dx * 2, y + dy * 2)
                if cheated_position in path:
                    time_here = steps_there[tile]
                    time_there = steps_there[cheated_position]
                    diff = time_there - time_here - 2
                    if diff >= 100:
                        part1 += 1
                
    # for k in cheats:
    #     v = cheats[k]
    #     print(k, v)

    print("Part 1:", part1)
    print("Part 2:", part2)