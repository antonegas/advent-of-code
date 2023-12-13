def into_dict(input):
    res = dict()
    data = list(input.split("\n"))
    for x in data:
        LR = dict()
        LR["L"] = x[7:10]
        LR["R"] = x[12:15]
        res[x[0:3]] = LR
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    data, keys = data.split("\n\n")

    res = 0
    d = into_dict(keys)
    current = "AAA"

    while True:
        for lr in data:
            res += 1
            current = d[current][lr]
            if current == "ZZZ":
                break
        if current == "ZZZ":
            break
            
    print("Part 1:", res)

