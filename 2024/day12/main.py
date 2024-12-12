def in_bound(g, c):
    x, y = c
    return x >= 0 and y >= 0 and x < len(g[0]) and y < len(g)

def dfs(m, x, y, v):
    l = m[y][x]
    
    v.add((x, y))
    res = {(x, y)}

    res_p = 4

    for pos in [p for p in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if in_bound(m, p)]:
        x2, y2 = pos
        if m[y2][x2] == l:
            res_p -= 1
            if (x2, y2) not in v:
                v.add((x2, y2))
                a, p = dfs(m, x2, y2, v)
                res.update(a)
                res_p += p

    return res, res_p

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    garden_plots = [[y for y in x] for x in data.split("\n")]

    part1 = 0
    part2 = 0

    visited = set()

    for y, l in enumerate(garden_plots):
        for x, p in enumerate(garden_plots):
            if (x, y) not in visited:
                a, p = dfs(garden_plots, x, y, visited)
                part1 += len(a) * p

    print("Part 1:", part1)
    print("Part 2:", part2)