import re

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    ms = re.findall("(do\\(\\))|(don\'t\\(\\))|(mul\\([0-9]+,[0-9]+\\))", data)

    p1 = 0
    p2 = 0

    do = True

    for m in ms:
        t = re.findall("[0-9]+", m[2])
        if m[0]:
            do = True
        elif m[1]:
            do = False
        elif do and m[2]:
            p2+= int(t[0]) * int(t[1])
        if m[2]:
            p1 += int(t[0]) * int(t[1])

    print("Part 1:", p1)
    print("Part 2:", p2)