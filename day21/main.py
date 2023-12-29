def get_starting_point(garden_map):
    for y, row in enumerate(garden_map):
        for x, col in enumerate(row):
            if col == "S":
                return (x, y)

def get_all_reachable(garden_map, steps):
    reachable_even = {get_starting_point(garden_map)}
    reachable_odd = set()
    new_reachable = reachable_even

    for i in range(steps):
        even = (i % 2) == 1
        reachables = set()
        for reachable in new_reachable:
            reachables.update(get_currently_reachable(garden_map, reachable))
        new_reachable = reachables.difference(reachable_even if even else reachable_odd)
        if even:
            reachable_even = reachable_even.union(reachables)
        else:
            reachable_odd = reachable_odd.union(reachables)

    return reachable_even if (steps % 2) == 0 else reachable_odd

def get_currently_reachable(garden_map, coordinate):
    res = list()
    x, y = coordinate

    for reachable in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        new_x, new_y = reachable
        if new_x >= 0 and new_x < len(garden_map[0]) and new_y >= 0 and new_y < len(garden_map) and garden_map[new_y][new_x] != "#":
            res.append(reachable)

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    garden_map = tuple(data.split("\n"))

    print("Part 1:", len(get_all_reachable(garden_map, 64)))
    print("Part 2:", 0)