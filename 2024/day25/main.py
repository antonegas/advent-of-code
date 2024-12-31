from itertools import product

def is_key(t):
    return t[0] == len(t[0]) * "."

def height(kl, ch):
    res = [-1] * len(kl[0])
    for y, l in enumerate(kl):
        for x, c in enumerate(l):
            if res[x] < 0 and c == ch:
                res[x] = y

    return res

def fits_wo_o(key, lock):
    for i in range(len(key)):
        if key[i] < lock[i]:
            return False
    return True

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    kl = [[y for y in x.split("\n")] for x in data.split("\n\n")]

    keys = [tuple(height(x, "#")) for x in kl if is_key(x)]
    locks = [tuple(height(x, ".")) for x in kl if not is_key(x)]

    part1 = 0
    part2 = 0

    for key, lock in product(keys, locks):
        if fits_wo_o(key, lock):
            part1 += 1
    
    print("Part 1:", part1)
    print("Part 2:", part2)