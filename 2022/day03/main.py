from collections import defaultdict

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    rs = [x for x in data.split("\n")]

    p1 = 0
    p2 = 0

    # print(rs)

    for r in rs:
        s1 = r[:int(len(r) / 2)]
        s2 = r[int(len(r) / 2):]
        # print(s1, s2)
        st = set()
        for l in s1:
            st.add(l)
        for l in s2:
            if l in st:
                if l.isupper():
                    t = ord(l) - ord('A') + 27
                    # print(t, l)
                    p1 += t
                else:
                    t = ord(l) - ord('a') + 1
                    # print(t, l)
                    p1 += t
                break

    c = int(len(rs) / 3)

    for i in range(0, len(rs), 3):
        d = defaultdict(lambda: 0)
        r1 = rs[i]
        r2 = rs[i + 1]
        r3 = rs[i + 2]

        # print(r1)
        # print(r2)
        # print(r3)
        # break

        m = min([len(k) for k in [r1, r2, r3]])

        print(m)

        for l in r1:
            if d[l] == 0:
                d[l] += 1

        for l in r2:
            if d[l] == 1:
                d[l] += 1

        for l in r3:
            if d[l] == 2:
                print(l)
                if l.isupper():
                    t = ord(l) - ord('A') + 27
                    # print(t, l)
                    p2 += t
                else:
                    t = ord(l) - ord('a') + 1
                    # print(t, l)
                    p2 += t
                break
            

        # for j in range(m):
        #     if r1 == r2 and r2 == r3:
                

    print("Part 1:", p1)
    print("Part 2:", p2)