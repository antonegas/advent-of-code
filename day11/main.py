ONE_MILLION = 1_000_000

def find_galaxies(universe):
    res = list()

    for y, row in enumerate(universe):
        for x, col in enumerate(row):
            if col == "#":
                res.append((x, y))

    return res

def row_contains_galaxy(universe, row: int):
    for col in universe[row]:
        if col == "#":
            return True
    return False

def col_contains_galaxy(universe, col: int):
    for row in universe:
        if row[col] == "#":
            return True

    return False

def find_shortest_path(universe, galaxy1, galaxy2):
    x_diff = galaxy2[0] - galaxy1[0]
    y_diff = galaxy2[1] - galaxy1[1]
    x = abs(x_diff)
    y = abs(y_diff)

    for col in range(min(0, x_diff), max(0, x_diff)):
        if not col_contains_galaxy(universe, galaxy1[0] + col):
            x += ONE_MILLION - 1

    for row in range(min(0, y_diff), max(0, y_diff)):
        if not row_contains_galaxy(universe, galaxy1[1] + row):
            y += ONE_MILLION - 1

    return x + y

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    universe = list(data.split("\n"))
    galaxies = find_galaxies(universe)

    s = 0

    for i,galaxy1 in enumerate(galaxies):
        for j,galaxy2 in enumerate(galaxies):
            s += find_shortest_path(universe, galaxy1, galaxy2)

    print("Part1:", s / 2)