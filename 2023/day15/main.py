def hashed(string):
    res = 0
    for char in string:
        res += ord(char)
        res *= 17
        res %= 256
    return res

def initialization(sequence):
    boxes = [dict() for _ in range(256)]
    for string in sequence:
        label, remove_operation, focal_length = hashmap(string)
        hashed_label = hashed(label)
        if not remove_operation:
            boxes[hashed_label][label] = focal_length
        elif label in boxes[hashed_label]:
            del boxes[hashed_label][label]
    return boxes

def hashmap(string):
    remove_operation = "-" in string
    label, focal_length = list(string.split("-")) if remove_operation else list(string.split("="))
    return label, remove_operation, focal_length

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    sequence = list(data.split(","))

    print("Part 1:", sum([hashed(string) for string in sequence]))
    print("Part 2:", sum([sum([(i + 1) * (j + 1) * int(focal_length) for j, focal_length in enumerate(box.values())]) for i, box in enumerate(initialization(sequence))]))