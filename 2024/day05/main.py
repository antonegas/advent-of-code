from collections import defaultdict

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    g = list(data.split("\n\n"))

    dic = defaultdict(lambda: set())

    for e in g[0].split("\n"):
        k, v = e.split("|")
        dic[int(k)].add(int(v))

    us = [[int(y) for y in x.split(",")] for x in g[1].split("\n")]


    p1 = 0
    p2 = 0

    for u in us:
        a = True
        c = set()
        fix = list()
        for i in range(len(u)):
            n = u[i]
            isec = dic[n].intersection(c)
            if len(isec) > 0:
                eir = 100000000
                for s in isec:

                    idx = fix.index(s)
                    if idx < eir:
                        eir = idx
                fix.insert(eir, n)
                c.add(n)
                a = False
            else:
                c.add(n)
                fix.append(n)

        if a:
            t = u[int((len(u) - 1) / 2)]
            
            p1 += t
        else:
            t2 = fix[int((len(fix) - 1) / 2)]
            p2 += t2

    print("Part 1:", p1)
    print("Part 2:", p2)