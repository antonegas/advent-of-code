from collections import deque

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    diagram = [[*x] for x in data.split("\n")]

    part1 = 0

    queue = deque([(diagram[0].index("S"), 0)])

    while queue:
        x, y = queue.popleft()

        n = 0

        if diagram[y][x] == "S" or diagram[y][x] == ".":
            n = 1
        else:
            n = int(diagram[y][x])

        if y + 1 >= len(diagram):
            continue

        y += 1

        if diagram[y][x] == "^":
            if diagram[y][x + 1].isnumeric():
                diagram[y][x + 1] = str(int(diagram[y][x + 1]) + n)
            else:
                diagram[y][x + 1] = str(n)
                queue.append((x + 1, y))
            if diagram[y][x - 1].isnumeric():
                diagram[y][x - 1] = str(int(diagram[y][x - 1]) + n)
            else:
                diagram[y][x - 1] = str(n)
                queue.append((x - 1, y))

            part1 += 1
        else:
            if diagram[y][x].isnumeric():
                diagram[y][x] = str(int(diagram[y][x]) + n)
            else:
                diagram[y][x] = str(n)
                queue.append((x, y))

    print("Part 1:", part1)
    print("Part 2:", sum([int(x) for x in diagram[-1] if x.isnumeric()]))