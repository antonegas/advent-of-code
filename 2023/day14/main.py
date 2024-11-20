DIRECTIONS = ["north", "south", "west", "east"]

def transpose(dish):
    res = []
    for row in zip(*dish):
        res.append("".join(row))
    return res

def mirror_vertically(dish):
    return list(reversed(dish))

def mirror_horizontally(dish):
    return ["".join(reversed(row)) for row in dish]

def remove_round_rocks(dish):
    res = []
    for row in dish:
        current_row = ""
        for col in row:
            current_row += "#" if col == "#" else "."
        res.append(current_row)
    return res

def slide_direction(dish, direction):
    if direction not in DIRECTIONS:
        raise Exception("Not a valid direction")
    changed_dish = dish
    # Change so it is as if it is sliding south
    if direction == "north":
        changed_dish = mirror_vertically(changed_dish)
    elif direction == "west":
        changed_dish = transpose(mirror_horizontally(changed_dish))
    elif direction == "east":
        changed_dish = transpose(changed_dish)

    changed_dish = slide(changed_dish)

    # Undo mirroring and transposing
    if direction == "north":
        changed_dish = mirror_vertically(changed_dish)
    elif direction == "west":
        changed_dish = mirror_horizontally(transpose(changed_dish))
    elif direction == "east":
        changed_dish = transpose(changed_dish)

    return changed_dish

def slide(dish):
    # Assumes direction is south
    res = list()
    temp = list()
    without_rocks = list(reversed(remove_round_rocks(dish)))
    falling_rocks = [0 for _ in dish[0]]
    
    # Calculate how many round rocks stacked in a column
    for row in dish:
        for x, col in enumerate(row):
            if col == "#" and falling_rocks[x] != 0:
                temp[-1][x] = falling_rocks[x]
                falling_rocks[x] = 0
            elif col == "O":
                    falling_rocks[x] += 1
        temp.append([0 for _ in dish[0]])
    temp = temp[:-1]
    temp.append(falling_rocks)
    temp = list(reversed(temp))

    rocks = [0 for _ in dish[0]]
    
    # Draw round rocks onto res
    for y, row in enumerate(temp):
        for x, col in enumerate(row):
            if temp[y][x] != 0:
                rocks[x] = temp[y][x]
            elif rocks[x] > 0:
                rocks[x] -= 1
        pass
        res.append("".join(["O" if rocks[i] > 0 else char for i, char in enumerate(without_rocks[y])]))

    return list(reversed(res))

def cycle(dish):
    res = slide_direction(dish, "north")
    res = slide_direction(res, "west")
    res = slide_direction(res, "south")
    res = slide_direction(res, "east")
    return res

def cycle_n(dish, n):
    res = dish
    previous = dict()
    n_to_repeat = -1
    i = 0
    while i < n:
        res = cycle(res)
        res_key = tuple(res)
        if i < 500:
            if res_key in previous.keys():
                first_occurence = previous[res_key]
                n_to_repeat = i - first_occurence
                i = n - (n - i) % n_to_repeat
            else:
                previous[res_key] = i
        i += 1

    return res

def total_load(dish):
    total = 0
    for i, row in enumerate(reversed(dish)):
        for col in row:
            if col == "O":
                total += 1 + i
    return total

if __name__ == "__main__":
    import os    
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    dish = list(data.split("\n"))

    print("Part 1:", total_load(slide_direction(dish, "north")))
    print("Part 2:", total_load(cycle_n(dish, 1_000_000_000)))