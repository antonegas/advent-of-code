def get_paths(forest):
    START = (1, 1)
    END = (len(forest[0]) - 2, len(forest) - 1)
    checked = {(1, 0)}
    current_paths = [[(1, 0)]]
    paths = list()
    current = START

    while len(current_paths) != 0:
        

        current = get_next(current, forest, checked)

    return paths

def expand_path(start, forest, checked):
    path = [start]

    current = start

    while not is_slope(current[0], current[1], forest):
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
    if (x - 1, y) not in checked and forest[y][x - 1] != "#" and forest[y][x - 1] != ">":
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

    print(expand_path((1, 1), forest, {(1, 0)}))
    print(forest[4][15])
    print(get_next_sliding(get_slopes(15, 3, forest)[0][0], get_slopes(15, 3, forest)[0][1], forest))

    print("Part 1:", 0)
    print("Part 2:", 0)