def in_bound(g, c):
    x, y = c
    return x >= 0 and y >= 0 and x < len(g[0]) and y < len(g)

def dfs1(m, x, y):
    i = m[y][x]

    if i == 9:
        return {(x, y)}
    
    res = set()

    for pos in [p for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if in_bound(m, p)]:
        x2, y2 = pos
        if m[y2][x2] == i + 1:
            res.update(dfs1(m, x2, y2))

    return res

def dfs2(m, x, y):
    i = m[y][x]

    if i == 9:
        return 1
    
    res = 0

    for pos in [p for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if in_bound(m, p)]:
        x2, y2 = pos
        if m[y2][x2] == i + 1:
            res += dfs2(m, x2, y2)

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    topological_map = [[int(x) for x in y] for y in data.split("\n")]

    part1 = 0
    part2 = 0

    for y, l in enumerate(topological_map):
        for x, i in enumerate(l):
            if i == 0:
                part1 += len(dfs1(topological_map, x, y))
                part2 += dfs2(topological_map, x, y)     

    print("Part 1:", part1)
    print("Part 2:", part2)