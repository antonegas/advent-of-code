def in_bounds(grid, x, y):
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

def xmas(grid, x, y):
    if grid[y][x] != "X":
        return 0
    
    res = 0

    if in_bounds(grid, x - 1, y) and in_bounds(grid, x - 2, y) and in_bounds(grid, x - 3, y):
        if grid[y][x - 1] + grid[y][x - 2] + grid[y][x - 3] == "MAS":
            res += 1

    if in_bounds(grid, x + 1, y) and in_bounds(grid, x + 2, y) and in_bounds(grid, x + 3, y):
        if grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3] == "MAS":
            res += 1

    if in_bounds(grid, x, y + 1) and in_bounds(grid, x, y + 2) and in_bounds(grid, x , y + 3):
        if grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x] == "MAS":
            res += 1

    if in_bounds(grid, x, y - 1) and in_bounds(grid, x, y - 2) and in_bounds(grid, x , y - 3):
        if "X" + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x] == "XMAS":
            res += 1

    if in_bounds(grid, x - 1, y - 1) and in_bounds(grid, x - 2, y - 2) and in_bounds(grid, x - 3, y - 3):
        if "X" + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3] == "XMAS":
            res += 1

    if in_bounds(grid, x + 1, y - 1) and in_bounds(grid, x + 1, y - 1) and in_bounds(grid, x + 3, y - 3):
        if "X" + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3] == "XMAS":
            res += 1

    if in_bounds(grid, x + 1, y + 1) and in_bounds(grid, x + 2, y + 2) and in_bounds(grid,x + 3, y + 3):
        if "X" + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3] == "XMAS":
            res += 1

    if in_bounds(grid, x - 1, y + 1) and in_bounds(grid, x - 2, y + 2) and in_bounds(grid, x - 3, y + 3):
        if "X" + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3] == "XMAS":
            res += 1

    return res

def x_mas(grid, x, y):
    if grid[y][x] != "A":
        return 0
    
    res = 0

    if in_bounds(grid, x + 1, y - 1) and in_bounds(grid, x - 1, y + 1):
        if grid[y - 1][x + 1] + "A" + grid[y + 1][x - 1] == "MAS":
            res += 1

    if in_bounds(grid, x - 1, y + 1) and in_bounds(grid, x + 1, y - 1):
        if grid[y + 1][x - 1] + "A" + grid[y - 1][x + 1] == "MAS":
            res += 1

    if in_bounds(grid, x - 1, y - 1) and in_bounds(grid, x + 1, y + 1):
        if grid[y - 1][x - 1] + "A" + grid[y +1][x + 1] == "MAS":
            res += 1

    if in_bounds(grid, x + 1, y + 1) and in_bounds(grid, x - 1, y - 1):
        if grid[y + 1][x + 1] + "A" + grid[y - 1][x - 1] == "MAS":
            res += 1

    return res == 2

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    grid = [x for x in data.split("\n")]

    part1 = 0
    part2 = 0

    for x in range(len(grid[0])):
        for y in range(len(grid)):
            part1 += xmas(grid, x, y)
            part2 += x_mas(grid, x, y)

    print("Part 1:", part1)
    print("Part 2:", part2)