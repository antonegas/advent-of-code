if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    heat_loss_map = list(list(x) for x in data.splitlines())

    print("Part 1:", 0)
    print("Part 2:", 0)