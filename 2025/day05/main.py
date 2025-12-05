if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    a, b = data.split("\n\n")

    ranges = [tuple(map(int, x.split("-"))) for x in a.split("\n")]
    ingredients = [*map(int,b.split("\n"))]

    part1 = 0

    ranges.sort()
    overlapped = [ranges[0]]

    for begin, end in ranges[1:]:
        last_begin, last_end = overlapped[-1]

        if begin <= last_end:
            overlapped[-1] = (last_begin, max(end, last_end))
        else:
            overlapped.append((begin, end))

    for i in ingredients:
        for b, e in overlapped:
            if i >= b and e >= i:
                part1 += 1
                break

    print("Part 1:", part1)
    print("Part 2:", sum([end - begin + 1 for begin, end in overlapped]))