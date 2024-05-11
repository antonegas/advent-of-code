def get_paths(forest):
    START = (1, 0)
    END = (len(forest[0]) - 2, len(forest) - 1)
    checked_slopes = set()
    current_paths = [START]
    paths = list()

    while len(current_paths) != 0:
        current_start = current_paths.pop(0)
        current_path = expand_path(current_start, forest, END)
        paths.append(current_path)
        current_end = current_path[-1]
        slopes = get_slopes(current_end[0], current_end[1], forest)
        current_paths.extend([slope for slope in slopes if slope not in checked_slopes])
        checked_slopes.update(set(slopes))

    return paths

def dfs1(path, paths):
    return len(path) + max(*[dfs1(connected_path, paths) for connected_path in connected_paths1(path, paths)], 0, 0)


def connected_paths1(path_from, paths):
    x, y = path_from[-1]
    possible_connections = [(x + 1, y), (x, y + 1)]
    res = list()

    for path_to in paths:
        path_to_start = path_to[0]
        if path_to_start in possible_connections:
            res.append(path_to)

    return res

def dfs2(path, paths, visited):
    temp = connected_paths2(path, paths, visited)
    return len(path) + max(*[dfs2(connected_path, paths, visited.union({tuple(path)})) for connected_path in temp], 0, 0)


def connected_paths2(path_from, paths, visited):
    x, y = path_from[-1]
    possible_connections = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    res = list()

    for path_to in paths:
        path_to_start = path_to[0]
        if path_to_start in possible_connections and tuple(path_to) not in visited:
            res.append(path_to)

    return res

def expand_path(start, forest, end):
    path = list()
    checked = set()
    current = start

    while (current == start or not is_slope(current[0], current[1], forest)) and current != (0, 0) and current != end:
        path.append(current)
        checked.add(current)
        current = get_next(current[0], current[1], forest, checked)
    
    return path

def is_slope(x, y, forest):
    SLOPES = "<>v^"
    return forest[y][x] in SLOPES

def get_next_sliding(x, y, forest):
    slope = forest[y][x]

    if slope == "<":
        return (x - 1, y)
    elif slope == ">":
        return (x + 1, y)
    elif slope == "^":
        return (x, y - 1)
    else:
        return (x, y + 1)

def get_slopes(x, y, forest):
    res = []

    if forest[y][x - 1] == "<":
        res.append((x - 1, y))
    if forest[y][x + 1] == ">":
        res.append((x + 1, y))
    if forest[y - 1][x] == "^":
        res.append((x, y - 1))
    if forest[y + 1][x] == "v":
        res.append((x, y + 1))

    return res

def get_next(x, y, forest, checked):
    if (x, y) == (1, 0):
        return (1, 1)
    elif is_slope(x, y, forest):
        return get_next_sliding(x, y, forest)
    elif (x - 1, y) not in checked and forest[y][x - 1] != "#" and forest[y][x - 1] != ">":
        return (x - 1, y)
    elif (x + 1, y) not in checked and forest[y][x + 1] != "#" and forest[y][x + 1] != "<":
        return (x + 1, y)
    elif (x, y - 1) not in checked and forest[y - 1][x] != "#" and forest[y - 1][x] != "v":
        return (x, y - 1)
    elif (x, y + 1) not in checked and forest[y + 1][x] != "#" and forest[y + 1][x] != "^":
        return (x, y + 1)
    
    return (0, 0)

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    forest = [x for x in data.split("\n")]
    paths = get_paths(forest)

    print("Part 1:", dfs1(paths[0], paths))
    print("Part 2:", dfs2(paths[0], paths, set()))