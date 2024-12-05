def in_bounds(g, x, y):
    return x >= 0 and y >= 0 and x < len(g[0]) and y < len(g)

def xmas(g, x, y):
    if g[y][x] != "X":
        return 0
    
    res = 0

    if in_bounds(g, x - 1, y) and in_bounds(g, x - 2, y) and in_bounds(g, x - 3, y):
        if g[y][x - 1] + g[y][x - 2] + g[y][x - 3] == "MAS":
            res += 1
    
    # if in_bounds(g, x - 1, y) and g[y][x - 1] == "M":
    #     if in_bounds(g, x - 2, y) and g[y][x - 2] == "A":
    #         if in_bounds(g, x - 3, y) and g[y][x - 3] == "S":
    #             res += 1

    if in_bounds(g, x + 1, y) and in_bounds(g, x + 2, y) and in_bounds(g, x + 3, y):
        if g[y][x + 1] + g[y][x + 2] + g[y][x + 3] == "MAS":
            res += 1

    # if in_bounds(g, x + 1, y) and g[y][x + 1] == "M":
    #     if in_bounds(g, x + 2, y) and g[y][x + 2] == "A":
    #         if in_bounds(g, x + 3, y) and g[y][x + 3] == "S":
    #             res += 1

    if in_bounds(g, x, y + 1) and in_bounds(g, x, y + 2) and in_bounds(g, x , y + 3):
        if g[y + 1][x] + g[y + 2][x] + g[y + 3][x] == "MAS":
            res += 1


    # if in_bounds(g, x, y + 1) and g[y + 1][x] == "M":
    #     if in_bounds(g, x, y + 2) and g[y + 2][x] == "A":
    #         if in_bounds(g, x , y + 3) and g[y + 3][x] == "S":
    #             res += 1

    if in_bounds(g, x, y - 1) and in_bounds(g, x, y - 2) and in_bounds(g, x , y - 3):
        if "X" + g[y - 1][x] + g[y - 2][x] + g[y - 3][x] == "XMAS":
            res += 1

    # if in_bounds(g, x, y - 1) and g[y - 1][x] == "M":
    #     if in_bounds(g, x, y - 2) and g[y - 2][x] == "A":
    #         if in_bounds(g, x , y - 3) and g[y - 3][x] == "S":
    #             res += 1

    if in_bounds(g, x - 1, y - 1) and in_bounds(g, x - 2, y - 2) and in_bounds(g, x - 3, y - 3):
        if "X" + g[y - 1][x - 1] + g[y - 2][x - 2] + g[y - 3][x - 3] == "XMAS":
            res += 1

    # if in_bounds(g, x - 1, y - 1) and g[y - 1][x - 1] == "M":
    #     if in_bounds(g, x - 2, y - 2) and g[y - 2][x - 2] == "A":
    #         if in_bounds(g, x - 3, y - 3) and g[y - 3][x - 3] == "S":
    #             res += 1

    if in_bounds(g, x + 1, y - 1) and in_bounds(g, x + 1, y - 1) and in_bounds(g, x + 3, y - 3):
        if "X" + g[y - 1][x + 1] + g[y - 2][x + 2] + g[y - 3][x + 3] == "XMAS":
            res += 1

    # if in_bounds(g, x + 1, y - 1) and g[y - 1][x + 1] == "M":
    #     if in_bounds(g, x + 1, y - 1) and g[y - 2][x + 2] == "A":
    #         if in_bounds(g, x + 3, y - 3) and g[y - 3][x + 3] == "S":
    #             res += 1

    if in_bounds(g, x + 1, y + 1) and in_bounds(g, x + 2, y + 2) and in_bounds(g,x + 3, y + 3):
        if "X" + g[y + 1][x + 1] + g[y + 2][x + 2] + g[y + 3][x + 3] == "XMAS":
            res += 1

    # if in_bounds(g, x + 1, y + 1) and g[y + 1][x + 1] == "M":
    #     if in_bounds(g, x + 2, y + 2) and g[y + 2][x + 2] == "A":
    #         if in_bounds(g,x + 3, y + 3) and g[y + 3][x + 3] == "S":
    #             res += 1

    if in_bounds(g, x - 1, y + 1) and in_bounds(g, x - 2, y + 2) and in_bounds(g, x - 3, y + 3):
        if "X" + g[y + 1][x - 1] + g[y + 2][x - 2] + g[y + 3][x - 3] == "XMAS":
            res += 1

    # if in_bounds(g, x - 1, y + 1) and g[y + 1][x - 1] == "M":
    #     if (in_bounds(g, x - 2, y + 2) and g[y + 2][x - 2]) == "A":
    #         if in_bounds(g, x - 3, y + 3) and g[y + 3][x - 3] == "S":
    #             res += 1

    return res

def x_mas(g, x, y):
    if g[y][x] != "A":
        return 0
    
    res = 0

    if in_bounds(g, x + 1, y - 1) and g[y - 1][x + 1] == "M":
        if in_bounds(g, x - 1, y + 1) and g[y + 1][x - 1] == "S":
            res += 1

    if in_bounds(g, x - 1, y + 1) and g[y + 1][x - 1] == "M":
        if in_bounds(g, x + 1, y - 1) and g[y - 1][x + 1] == "S":
            res += 1

    if in_bounds(g, x - 1, y - 1) and g[y - 1][x - 1] == "M":
        if in_bounds(g, x + 1, y + 1) and g[y +1][x + 1] == "S":
            res += 1

    if in_bounds(g, x + 1, y + 1) and g[y + 1][x + 1] == "M":
        if in_bounds(g, x - 1, y - 1) and g[y - 1][x - 1] == "S":
            res += 1

    return res == 2

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    g = [x for x in data.split("\n")]

    p1 = 0
    p2 = 0

    for x in range(len(g[0])):
        for y in range(len(g)):
            p1 += xmas(g, x, y)
            p2 += x_mas(g, x, y)

    print("Part 1:", p1)
    print("Part 2:", p2)