if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    e = [sum([int(y) for y in x.split("\n")]) for x in data.split("\n\n")]

    print("Part 1:", max(e))
    print("Part 2:", sum(sorted(e)[-3:]))