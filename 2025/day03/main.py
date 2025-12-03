def maximize_joltage(bank: list[int], battery_count: int) -> int:
    offset = 0
    result = 0

    for safety in reversed(range(battery_count)):
        largest = 0

        for index, value in enumerate(bank[offset:len(bank) - safety], offset):
            if value > largest:
                offset = index + 1
                largest = value

            if largest == 9:
                break

        result += largest * 10**safety

    return result

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    banks = [[*map(int, x)] for x in data.split("\n")]

    print("Part 1:", sum([maximize_joltage(bank, 2) for bank in banks]))
    print("Part 2:", sum([maximize_joltage(bank, 12) for bank in banks]))