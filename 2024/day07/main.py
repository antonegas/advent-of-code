def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    te = [[y for y in x.split(": ")] for x in data.split("\n")]
    eqs = list()
    for t in te:
        e, ns = t
        eqs.append([int(e), [int(n) for n in ns.split(" ")]])

    part1 = 0
    part2 = 0
    for e, ns in eqs:
        found = False
        # print(e, ns)
        # t.append(2 ** (len(ns) - 1))
        for i in range(2 ** (len(ns) - 1)):
            bt = bin(i)[2:]
            b = bt.rjust(len(ns) - 1, '0')
            res = ns[0]
            # print(res, e, ns)
            for idx, bo in enumerate(b):
                if res > e:
                    break
                if bo == "1":
                    res += ns[idx + 1]
                else:
                    res *= ns[idx + 1]

            if res == e:
                # print(2 ** (len(ns) - 1))
                # print(b, e, ns)
                found = True
                break
        if found:
            # t.append(e)
            part1 += e
        
        found = False

        for i in range(3 ** (len(ns) - 1)):
            tt = ternary(i)
            t = tt.rjust(len(ns) - 1, '0')
            res = ns[0]

            for idx, to in enumerate(t):
                if res > e:
                    break
                if to == "2":
                    res = int(str(res) + str(ns[idx + 1]))
                elif to == "1":
                    res += ns[idx + 1]
                else:
                    res *= ns[idx + 1]

            if res == e:
                found = True
                break

        if found:
            part2 += e

    # print(max(t))

    print("Part 1:", part1)
    print("Part 2:", part2)