import re

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    clawmachines = [[list(map(int, re.findall(r"\d+", y))) for y in x.split("\n")] for x in data.split("\n\n")]

    part1 = 0
    part2 = 0

    for clawmachine in clawmachines:
        A, B, P = clawmachine
        x1, y1 = A
        x2, y2 = B
        c1, d1 = P

        c2 = c1 + 10000000000000
        d2 = d1 + 10000000000000

        a1 = (y2 * c1 - x2 * d1) / (x1 * y2 - x2 * y1)
        b1 = (-y1 * c1 + x1 * d1) / (x1 * y2 - x2 * y1)

        a2 = (y2 * c2 - x2 * d2) / (x1 * y2 - x2 * y1)
        b2 = (-y1 * c2 + x1 * d2) / (x1 * y2 - x2 * y1)

        if a1 == int(a1) and b1 == int(b1):
            prize1 = int(a1 * 3 + b1)
            part1 += prize1

        if a2 == int(a2) and b2 == int(b2):
            prize2 = int(a2 * 3 + b2)
            part2 += prize2

    print("Part 1:", part1)
    print("Part 2:", part2)