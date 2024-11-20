def get_starting_point(garden_map):
    for y, row in enumerate(garden_map):
        for x, col in enumerate(row):
            if col == "S":
                return (x, y)

def get_all_reachable(garden_map, steps):
    res = list()
    reachable_even = {get_starting_point(garden_map)}
    reachable_odd = set()
    new_reachable = reachable_even

    for i in range(1, max(steps) + 1):
        even = (i % 2) == 0
        reachables = set()
        for reachable in new_reachable:
            reachables.update(get_currently_reachable(garden_map, reachable))
        new_reachable = reachables.difference(reachable_even if even else reachable_odd)
        if even:
            reachable_even = reachable_even.union(reachables)
        else:
            reachable_odd = reachable_odd.union(reachables)
        if i in steps:
            res.append(len(reachable_even if even else reachable_odd))

    return res

def get_currently_reachable(garden_map, coordinate):
    res = list()
    x, y = coordinate
    height = len(garden_map)
    width = len(garden_map[0])

    for reachable in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        new_x, new_y = reachable
        if garden_map[new_y % height][new_x % width] != "#":
            res.append(reachable)

    return tuple(res)

def quadratic_coefficients(y: tuple[int, int, int]):
    y0, y1, y2 = y
    return y0, (-3 * y0 + 4 * y1 - y2) // 2, (y0 - 2 * y1 + y2) // 2

def calculate_quadratic(x, coefficients):
    c, b, a = coefficients
    return c + b * x + a * x**2


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    garden_map = tuple(data.split("\n"))

    print("Part 1:", get_all_reachable(garden_map, [64])[0])
    print("Part 2:", calculate_quadratic(202300, quadratic_coefficients(get_all_reachable(garden_map, [65, 196, 327]))))