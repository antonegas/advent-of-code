def count_pointing_zero(sequence: list[tuple[str, int]]):
    dial = 50
    result = 0

    for direction, distance in sequence:
        if direction == "L":
            dial -= distance
        else:
            dial += distance

        dial = dial % 100

        if dial == 0:
            result += 1

    return result

def count_passing_zero(sequence: list[tuple[str, int]]):
    dial = 50
    result = 0

    for direction, distance in sequence:
        result += distance // 100

        if direction == "L":
            if dial == 0:
                result -= 1

            if (dial - distance) % 100 > dial or (dial - distance) % 100 == 0:
                result += 1

            dial -= distance
        else:
            if (dial + distance) % 100 < dial:
                result += 1
            
            dial += distance

        dial = dial % 100

    return result

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    sequence = [(x[0], int(x[1:])) for x in data.split("\n")]

    print("Part 1:", count_pointing_zero(sequence))
    print("Part 2:", count_passing_zero(sequence))