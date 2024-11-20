from math import floor, ceil, sqrt
from functools import reduce

def ways_to_win(time, distance):
    offset = sqrt((time * time / 4 - distance - 1))
    return floor(time / 2 + offset) - ceil(time / 2 - offset) + 1

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    times, distances = list(list(int(y) for y in " ".join(x.split()).split(" ")[1:]) for x in data.split("\n"))

    print("Part 1:", reduce(lambda a, b: a * b, [ways_to_win(time, distance) for time, distance in zip(times, distances)]))
    print("Part 2:", ways_to_win(int("".join(map(str, times))), int("".join(map(str, distances)))))