DIGITS = "0123456789"

def adjecent_to_symbol(schematic, x, y):
    height = len(schematic)
    width = len(schematic[0])
    temp = "".join([line[max(x - 1, 0):min(x + 2, width)] for line in schematic[max(y - 1, 0):min(y + 2, height)]])
    
    for letter in temp:
        if letter not in DIGITS + ".":
            return True

    return False

def get_possible_gears(schematic):
    res = list()

    for y, line in enumerate(schematic):
        for x, letter in enumerate(line):
            if letter == "*":
                res.append((x, y))

    return res

def numbers_adjecent_to_gear(schematic, gear):
    """ Assumes numbers are never bigger than 3 digits """
    res = list()
    height = len(schematic)
    width = len(schematic[0])
    x, y = gear
    should_add = False
    current = ""

    for line in schematic[max(y - 1, 0):min(y + 2, height)]:
        for _x, letter in enumerate(line[max(x - 3, 0):min(x + 4, width)]):
            if letter in DIGITS:
                current += letter
                # Magic numbers for if the index is in the center +-1
                if 2 <= _x <= 4:
                    should_add = True
            else:
                if should_add:
                    res.append(int(current))
                should_add = False
                current = ""
        if should_add:
            res.append(int(current))
        should_add = False
        current = ""

    return res

def get_part_numbers(schematic):
    res = list()
    should_add_current = False
    current = ""

    for y, line in enumerate(schematic):
        for x, letter in enumerate(line):
            if letter in DIGITS:
                current += letter
                if adjecent_to_symbol(schematic, x, y):
                    should_add_current = True
            else:
                if should_add_current:
                    res.append(int(current))
                current = ""
                should_add_current = False
        if should_add_current:
            res.append(int(current))
        current = ""
        should_add_current = False
        
    return res

def get_gear_ratios(schematic):
    res = list()
    gears = get_possible_gears(schematic)

    for gear in gears:
        gear_numbers = numbers_adjecent_to_gear(schematic, gear)
        if len(gear_numbers) == 2:
            res.append(gear_numbers[0] * gear_numbers[1])

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    schematic = list(data.split("\n"))

    print("Part 1:", sum(get_part_numbers(schematic)))
    print("Part 2:", sum(get_gear_ratios(schematic)))