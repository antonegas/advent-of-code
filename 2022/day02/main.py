if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    inp = [[y for y in x.split(" ")] for x in data.split("\n")]

    # print(inp)

    sc = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    w = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        }
    }

    sc2 = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    sc3 = {
        "A": {
            0: "Z",
            3: "X",
            6: "Y",
        },
        "B": {
            0: "X",
            3: "Y",
            6: "Z",
        },
        "C": {
            0: "Y",
            3: "Z",
            6: "X",
        }
    }

    p1 = 0

    p2 = 0

    for o, y in inp:
        # print(sc[y], w[o][y])
        p1 += sc[y]
        p1 += w[o][y]

    for o, y in inp:
        t = sc2[y]
        p2 += t
        p2 += sc[sc3[o][t]]

    print("Part 1:", p1)
    print("Part 2:", p2)