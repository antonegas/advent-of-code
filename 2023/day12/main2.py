from functools import cache

@cache
def possible_count(springs: str, groups: tuple[int, ...], must_be_damaged: bool, must_be_operational: bool):
    """ Recursively """
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0
    if len(groups) == 0:
        if "#" in springs:
            return 0
        else:
            return 1
    
    current = springs[0]
    rest = springs[1:]

    if current == "#":
        if must_be_operational:
            return 0
        updated_groups = groups[1:]
            
        if groups[0] > 1:
            return possible_count(rest, (groups[0] - 1,) + updated_groups, True, False)
        else:
            return possible_count(rest, updated_groups, False, True)
        
    if current == ".":
        if must_be_damaged:
            return 0
        return possible_count(rest, groups, False, False)
    if current == "?":
        return possible_count("#" + rest, groups, must_be_damaged, must_be_operational) + possible_count("." + rest, groups, must_be_damaged, must_be_operational)


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    data_lines = list(data.split("\n"))

    sum1 = 0

    for line in data_lines:
        springs, groups = line.split(" ")
        groups = tuple(map(int, groups.split(",")))
        sum1 += possible_count(springs, groups, False, False)

    sum2 = 0

    for line in data_lines:
        springs, groups = line.split(" ")
        springs = "?".join([springs] * 5)
        groups = ",".join([groups] * 5)
        groups = tuple(map(int, groups.split(",")))
        sum2 += possible_count(springs, groups, False, False)

    print("Part 1:", sum1)
    print("Part 2:", sum2)