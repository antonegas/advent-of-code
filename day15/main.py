def hashed(string):
    res = 0
    for char in string:
        res += ord(char)
        res *= 17
        res %= 256
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    sequence = list(data.split(","))

    print("Part 1:", sum([hashed(string) for string in sequence]))