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
    towels_data, designs_data = data.split("\n\n")

    towels = tuple(towels_data.split(", "))
    designs = tuple(designs_data.split("\n"))


    print("Part 1:", len([design for design in designs if dfs1(towels, design)]))
    print("Part 2:", sum([dfs2(towels, design) for design in designs]))