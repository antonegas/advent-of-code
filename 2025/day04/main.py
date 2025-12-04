if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    grid = [list(x) for x in list(data.split("\n"))]

    part1 = 0
    part2 = 0

    removed = True
    first = True

    while removed:
        removed = False
        copied_grid = [x[:] for x in grid]

        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] != "@":
                    continue

                count = 0
                
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if x + dx < 0 or x + dx >= len(grid[0]):
                            continue
                        if y + dy < 0 or y + dy >= len(grid):
                            continue

                        if grid[y + dy][x + dx] == "@":
                            count += 1

                if count < 4:
                    copied_grid[y][x] = "."
                    removed = True

                    part1 += first
                    part2 += 1

        first = False
        grid = copied_grid

    print("Part 1:", part1)
    print("Part 2:", part2)