import re

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    ms = re.findall(r"(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))", data)

    part1 = 0
    part2 = 0

    do = True

    for m in ms:
        t = re.findall(r"\d+", m[2])
        if m[0]:
            do = True
        elif m[1]:
            do = False
        elif do and m[2]:
            part2 += int(t[0]) * int(t[1])
        if m[2]:
            part1 += int(t[0]) * int(t[1])

    print("Part 1:", part1)
    print("Part 2:", part2)