def in_bound(width, height, coord):
    x, y = coord
    return x >= 0 and y >= 0 and x <= width and y <= height

def bfs(maze, start, end):
    queue = [start]
    steps = {start: 0}

    while len(queue) > 0:
        coord = queue.pop(0)
        if coord == end:
            return steps
        x, y = coord
        for n in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            x2, y2 = n
            if n not in steps and in_bound(len(maze[0]), len(maze), coord) and maze[y2][x2] != "#":
                steps[n] = steps[coord] + 1
                queue.append(n)

    return steps

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

    steps = bfs(maze, start, end)

    for tile1 in steps:
        x, y = tile1
        for dy in range(-20, 21):
            for dx in range(-(20 - abs(dy)), 21 - abs(dy)):
                diff = abs(dx) + abs(dy)
                tile2 = (x + dx, y + dy)
                if tile2 not in steps:
                    continue
                save = steps[tile2]- steps[tile1] - diff
                if save < 100:
                    continue
                if diff == 2:
                    part1 += 1
                part2 += 1

    print("Part 1:", part1)
    print("Part 2:", part2)