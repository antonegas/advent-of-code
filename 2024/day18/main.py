if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()



    part1 = 0
    part2 = 0



    print("Part 1:", part1)
    print("Part 2:", part2)