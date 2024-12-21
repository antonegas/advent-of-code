from collections import defaultdict

NUMERIC_KEYPAD = [
    "789",
    "456",
    "123",
    " 0A",
]

DIRECTIONAL_KEYPAD = [
    " ^A",
    "<v>"
]

DIRECTIONS = {
    (0, 1): "v",
    (0, -1): "^",
    (1, 0): ">",
    (-1, 0): "<"
}

def get_keypad_dict(keypad):
    keypad_dict = defaultdict(lambda: dict())
    previous = defaultdict(lambda: dict())

    coords = []

    for y, l in enumerate(keypad):
        for x, c in enumerate(l):
            if c != " ":
                coords.append((x, y))

    for coord_from in coords:
        for coord_to in coords:
            if coord_from == coord_to:
                keypad_dict[coord_from][coord_to] = 0
                previous[coord_from][coord_to] = coord_from
            elif next_to(coord_from, coord_to):
                keypad_dict[coord_from][coord_to] = 1
                previous[coord_from][coord_to] = coord_from
            else:
                keypad_dict[coord_from][coord_to] = float('inf')
                previous[coord_from][coord_to] = None

    return keypad_dict, previous

def get_key_pos(keypad, key):
    for y, l in enumerate(keypad):
        for x, c in enumerate(l):
            if c == key:
                return (x, y)
    return (-1, -1)

def next_to(key1_pos, key2_pos):
    x1, y1 = key1_pos
    x2, y2 = key2_pos

    return abs(x1 - x2) + abs(y1 - y2) == 1


def floyd_warshall(keypad):
    keypad_dict, previous = get_keypad_dict(keypad)

    for k in keypad_dict:
        for i in keypad_dict:
            for j in keypad_dict:
                if keypad_dict[i][j] > keypad_dict[i][k] + keypad_dict[k][j]:
                    keypad_dict[i][j] = keypad_dict[i][k] + keypad_dict[k][j]
                    previous[i][j] = previous[k][j]

    return previous

def get_path(previous, start, end):
    if previous[start][end] == None:
        return []
    path = [end]
    while start != end:
        end = previous[start][end]
        path = [end] + path
    return path

def get_paths(previous_coords):
    paths = defaultdict(lambda: dict())

    for coord_from in previous_coords:
        for coord_to in previous_coords:
            paths[coord_from][coord_to] = get_path(previous_coords, coord_from, coord_to)

    return paths

def numberic_part(code):
    return int(code[:3])

def full_code_directions(numberic_paths, directional_paths, code):
    numeric_directions = ""
    previous_key = "A"

    for key in code:
        numeric_directions += numberic_paths[previous_key][key] + "A"
        previous_key = key

    directional_directions = ""
    previous_key = "A"

    for key in numeric_directions:
        directional_directions += directional_paths[previous_key][key] + "A"
        previous_key = key

    my_directions = ""
    previous_key = "A"

    for key in directional_directions:
        my_directions += directional_paths[previous_key][key] + "A"
        previous_key = key

    return my_directions

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    codes = list(data.split("\n"))

    part1 = 0
    part2 = 0

    numeric_previous = floyd_warshall(NUMERIC_KEYPAD)
    directional_previous = floyd_warshall(DIRECTIONAL_KEYPAD)
    numeric_paths = get_paths(numeric_previous)
    directional_paths = get_paths(directional_previous)

    current = "A"
    code_directions = ""

    for code in codes:
        print(full_code_directions(numeric_paths, directional_paths, code))


    print("Part 1:", part1)
    print("Part 2:", part2)