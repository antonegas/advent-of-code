from functools import cache

@cache
def dfs1(towels, design):
    if len(design) == 0:
        return True

    for towel in towels:
        if towel == design[:len(towel)] and dfs1(towels, design[len(towel):]):
            return True

    return False

@cache
def dfs2(towels, design):
    if len(design) == 0:
        return 1
    
    res = 0

    for towel in towels:
        if towel == design[:len(towel)]:
            res += dfs2(towels, design[len(towel):])

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    towels, designs = [(tuple(x.split(", ")), tuple(y.split("\n"))) for x, y in [tuple(data.split("\n\n"))]][0]

    print("Part 1:", len([design for design in designs if dfs1(towels, design)]))
    print("Part 2:", sum([dfs2(towels, design) for design in designs]))