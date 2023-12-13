DIGITS = "123456789"
DIGITS_SPELT = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIGITS_DICT = {DIGITS_SPELT[i]: DIGITS[i] for i in range(len(DIGITS))}

def first(line):
    for letter in line:
        if letter in DIGITS:
            return letter
        
def last(line):
    digit = "0"
    for letter in line:
        if letter in DIGITS:
            digit = letter
    return digit

def first2(line):
    for i in range(len(line)):
        letter = line[i]
        if letter in DIGITS:
            return letter
        else:
            temp = digit_spelt(line, i)
            if temp is not None:
                return temp

def last2(line):
    res = "0"
    for i in range(len(line)):
        letter = line[i]
        if letter in DIGITS:
            res = letter
        else:
            temp = digit_spelt(line, i)
            if temp is not None:
                res = temp
    return res

def digit_spelt(line, i):
    for digit in DIGITS_SPELT:
                digit_in_line = line[i:i + len(digit)]
                if digit_in_line == digit:
                    return DIGITS_DICT[digit]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    lines = list(data.split("\n"))

    s1 = 0

    for line in lines:
        s1 += int(first(line) + last(line))

    s2 = 0

    for line in lines:
        s2 += int(first2(line) + last2(line))

    print("Part 1:", s1)
    print("Part 2:", s2)