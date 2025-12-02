if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    ranges = [tuple(map(int, x.split("-"))) for x in data.split(",")]

    part1 = 0
    part2 = 0

    for start, end in ranges:
        for identifier in range(start, end + 1):
            string = str(identifier)

            if string[:len(string) // 2] == string[len(string) // 2:]:
                part1 += identifier

            for j in range(1, len(string) // 2 + 1):
                if len(string) % j:
                    continue

                if string[:j] * (len(string) // j) == string:
                    part2 += identifier
                    break

    print("Part 1:", part1)
    print("Part 2:", part2)