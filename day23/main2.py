from collections import defaultdict


def is_intersection(coordinate, forest):
    return len(get_connected(coordinate, forest)) > 2

def is_wall(coordinate, forest):
    x, y = coordinate
    return forest[y][x] == "#"

def get_end(forest):
    return (len(forest[0]) - 2, len(forest) - 1)

def get_start():
    return (1, 0)

def is_end(coordinate, forest):
    return get_end(forest) == coordinate

def is_start(coordinate):
    return get_start() == coordinate

def get_adjecent(coordinate):
    x, y = coordinate
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}

def in_bounds(coordinate, forest):
    x, y = coordinate
    return x >= 0 and y >= 0 and x < len(forest[0]) and y < len(forest)

def get_connected(coordinate, forest):
    return set(adjecent for adjecent in get_adjecent(coordinate) if in_bounds(adjecent, forest) and not is_wall(adjecent, forest))

def get_next(coordinate, forest, visited):
    return get_connected(coordinate, forest).difference(visited)

def get_path(intersection, entry_point, forest):
    visited = {intersection}
    path = []
    current = entry_point

    while not is_end(current, forest) and not is_start(current) and not is_intersection(current, forest):
        visited.add(current)
        path.append(current)
        current = get_next(current, forest, visited).pop()

    path.append(current)
    return path

def place(coordinate, forest, letter):
    x, y = coordinate
    forest[y] = forest[y][:x] + letter + forest[y][x + 1:]
    return forest

def print_forest(forest):
    for row in forest:
        print(row)

def get_paths(forest): # bfs
    visited = set()
    queue = list()
    queue.append(get_start())
    visited.add(get_start())
    paths = defaultdict(lambda: dict())

    while len(queue) != 0:
        current_intersection = queue.pop(0)
        for exit_point in get_connected(current_intersection, forest):
            path = get_path(current_intersection, exit_point, forest)
            other_intersection = path[-1]

            paths[current_intersection][other_intersection] = len(path)
            paths[other_intersection][current_intersection] = len(path)

            if other_intersection not in visited:
                visited.add(other_intersection)
                queue.append(other_intersection)

    return paths

def dfs(intersection, paths, visited, end):
    if intersection == end:
        return 0

    visited.add(intersection)
    # print(intersection, visited)

    possible_paths = set(paths[intersection]).difference(visited)

    if len(possible_paths) == 0:
        return float('-inf')

    # for possible_path in possible_paths:
    #     dfs(possible_path, paths, visited.copy(), end)

    return max([dfs(possible_path, paths, visited.copy(), end) + paths[intersection][possible_path] for possible_path in possible_paths])

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    forest = [x for x in data.split("\n")]

    # print(dict(get_paths(forest)))

    temp = forest
    d = get_paths(forest)
    # print(d)

    # abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # for i, x in enumerate(d):
    #     place(x, temp, abc[i])

    # print(set(d))

    # print_forest(temp)

    print(dfs(get_start(), d, set(), get_end(forest)))

    # print_forest(place((19, 20), forest, "O"))

    print("Part 1:", 0)
    print("Part 2:", 0)