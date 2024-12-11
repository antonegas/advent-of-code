if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    stones = [int(x) for x in data.split(" ")]

    part1 = 0
    part2 = 0

    stones1 = stones[:]

    for i in range(75):
        r = list()
        for stone in stones1:
            if stone == 0:
                r.append(1)
            elif len(str(stone)) % 2 == 0:
                t = str(stone)
                r.append(int(t[:len(t)//2]))
                r.append(int(t[len(t)//2:]))
            else:
                r.append(stone * 2024)
        stones1 = r

    print("Part 1:", len(stones1))
    print("Part 2:", part2)