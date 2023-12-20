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

def rows_containing_galaxies(galaxies):
    return set(galaxy[1] for galaxy in galaxies)

def cols_containing_galaxies(galaxies):
    return set(galaxy[0] for galaxy in galaxies)

def col_contains_galaxy(universe, col: int):
    for row in universe:
        if row[col] == "#":
            return True

    return False

def find_shortest_path(galaxy1, galaxy2, rows_with_galaxies, cols_with_galaxies, expansion_rate):
    x_diff = galaxy2[0] - galaxy1[0]
    y_diff = galaxy2[1] - galaxy1[1]
    x_distance = 0
    y_distance = 0

    for col_offset in range(min(0, x_diff), max(0, x_diff)):
        col = galaxy1[0] + col_offset
        if col in cols_with_galaxies:
            x_distance += 1
        else:
            x_distance += expansion_rate

    for row_offset in range(min(0, y_diff), max(0, y_diff)):
        row = galaxy1[1] + row_offset
        if row in rows_with_galaxies:
            y_distance += 1
        else:
            y_distance += expansion_rate

    return x_distance + y_distance

def find_shortest_paths(universe, expansion_rate):
    res = list()
    galaxies = find_galaxies(universe)
    rows_with_galaxies = rows_containing_galaxies(galaxies)
    cols_with_galaxies = cols_containing_galaxies(galaxies)

    for i, galaxy1 in enumerate(galaxies):
        for galaxy2 in galaxies[i + 1:]:
            res.append(find_shortest_path(galaxy1, galaxy2, rows_with_galaxies, cols_with_galaxies, expansion_rate))

    return res


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    universe = list(data.split("\n"))

    print("Part 1:", sum(find_shortest_paths(universe, 2)))
    print("Part 2:", sum(find_shortest_paths(universe, 1_000_000)))