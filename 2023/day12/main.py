def unfold(record):
    string, groups = record
    res_string = string + "?" + string + "?" + string + "?" + string + "?" + string
    return res_string, groups * 5

def is_valid(string, groups):
    temp = list(len(y) for y in filter(lambda x: x != "", string.split(".")))

    if len(temp) != len(groups):
        return False

    for a, b in zip(temp, groups):
        if a != b:
            return False
    return True

def filled_binary(length, number):
    temp = bin(number)[2:].replace("0", ".").replace("1", "#")
    return (length - len(temp)) * "." + temp

def generate_guesses(string):
    length = string.count("?")
    res = list()

    if length == 0:
        return res

    for i in range(2**length):
        res.append(filled_binary(length, i))
    
    return res

def num_valid(record):
    string, groups = record
    return len(list(x for x in generate_guesses(string) if is_valid(insert_guess(string, x), groups)))

def insert_guess(string, guess):
    res = string
    for value in guess:
        res = res.replace("?", value, 1)
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    condition_records: list[tuple[str, list[int]]] = list((x.split(" ")[0], list(int(y) for y in x.split(" ")[1].split(","))) for x in data.split("\n"))

    print("Part 1:", sum(list(num_valid(x) for x in condition_records)))
    # print("Part 2:", sum(list(num_valid(unfold(x)) for x in condition_records)))