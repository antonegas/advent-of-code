def invert(n, i):
    if n & (1 << i):
        n -= 1 << i
    else:
        n += 1 << i

    return n

def to_bin(l):
    return int(''.join(map(str, l)), 2)

def press(n, p):
    for x in p:
        n = invert(n, x)
    return n

if __name__ == "__main__":
    from os import path
    data = open(path.join(path.dirname(__file__), "input.txt"), "r").read()

    manual = list()

    for x, *y, z in [[*x.split(" ")] for x in data.split("\n")]:
        x = tuple(reversed([1 if a == "#" else 0 for a in x[1:-1]]))
        y = tuple([tuple(map(int, a[1:-1].split(","))) for a in y])
        z = tuple([*map(int, z[1:-1].split(","))])
        manual.append((x, y, z))

    part1 = 0
    part2 = 0

    for target, options, _ in manual:
        table = [0] * 2**len(target)
        table[0] = 1

        depth = 0

        while table[to_bin(target)] == 0:
            other = table[:]
            for n in range(2**len(target)):
                if table[n] == 0:
                    continue
                if n == 25:
                    pass

                for option in options:
                    index = press(n, option)
                    other[index] = 1

            table = other

            depth += 1

        part1 += depth

    print("Part 1:", part1)
    print("Part 2:", part2)