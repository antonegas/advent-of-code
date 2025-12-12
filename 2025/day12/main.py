if __name__ == "__main__":
    from os import path
    data = open(path.join(path.dirname(__file__), "input.txt"), "r").read()
    *_, x = data.split("\n\n")

    part1 = 0
    part2 = 0

    for l in x.split("\n"):
        y, z = l.split(": ")
        w, h = map(int, y.split("x"))
        counts = list(map(int, z.split(" ")))

        area = w * h

        if 9 * sum(counts) <= area:
            part1 += 1
    
    print("Part 1:", part1)
    print("Part 2:", part2)