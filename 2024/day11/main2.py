from functools import cache

@cache
def blink_n(stone, loops):
    if loops == 0:
        return 1
    
    if stone == 0:
        return blink_n(1, loops - 1)
    elif len(str(stone)) % 2 == 0:
        t = str(stone)
        return blink_n(int(t[:len(t)//2]), loops - 1) + blink_n(int(t[len(t)//2:]), loops - 1)
    else:
        return blink_n(stone * 2024, loops - 1)

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    stones = [int(x) for x in data.split(" ")]

    print("Part 1:", sum([blink_n(stone, 75) for stone in stones]))
    print("Part 2:", sum([blink_n(stone, 75) for stone in stones]))