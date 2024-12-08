from collections import defaultdict

def in_bound(g, c):
    x, y = c
    return x >= 0 and y >= 0 and x < len(g[0]) and y < len(g)

def antinodes(g, a1, a2):
    dx = a1[0] - a2[0]
    dy = a1[1] - a2[1]

    temp = list()

    mx = len(g[0]) // abs(dx)
    my = len(g) // abs(dy)

    for m in range(0, max(mx, my) + 1):
        temp.extend([(a1[0] + dx * m, a1[1] + dy * m), (a2[0] - dx * m, a2[1] - dy * m)])

    res = [x for x in temp if in_bound(g, x)]

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    g = [x for x in data.split("\n")]

    part1 = 0
    part2 = 0

    locations = set()
    antennas = defaultdict(list)

    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] != ".":
                antennas[g[y][x]].append((x, y))

    for k in antennas:
        for a1 in range(len(antennas[k])):
            for a2 in range(a1 + 1, len(antennas[k])):
                locations.update(antinodes(g, antennas[k][a1], antennas[k][a2]))
        # for a1, a2 in zip(antennas[k], antennas[k][1:]):
            
    # print(antinodes(g, (0, 0), (1, 2)))
    # print(in_bound(g, (5, 10)), len(g), len(g[0]))

    print("Part 1:", len(locations))
    print("Part 2:", part2)