from functools import cache

num_keypad = [
    "789",
    "456",
    "123",
    " 0A"
]
dir_keypad = [
    " ^A",
    "<v>"
]

def get_key_position(keypad, key):
    for y, keypad_line in enumerate(keypad):
        for x, keypad_key in enumerate(keypad_line):
            if keypad_key == key:
                return (x, y)
            
    return (-1, -1)

def get_possible_presses(keypad, from_key, to_key):
    from_x, from_y = from_key
    to_x, to_y = to_key
    dx = to_x - from_x
    dy = to_y - from_y

    possible_presses = set()

    if keypad[from_y][from_x + dx] != " ":
        possible_presses.add(">" * dx + "<" * -dx + "v" * dy + "^" * -dy + "A")
    if keypad[from_y + dy][from_x] != " ":
        possible_presses.add("v" * dy + "^" * -dy + ">" * dx + "<" * -dx + "A")

    return possible_presses

def shortest_numeric_sequence(code, number_of_robots):
    previous_key_position = get_key_position(num_keypad, "A")

    sequence_length = 0

    for key in code:
        current_key_position = get_key_position(num_keypad, key)
        shortest_resulting_length = float('inf')
        possible_presses = get_possible_presses(num_keypad, previous_key_position, current_key_position)

        for keypresses in possible_presses:
            resulting_sequence_length = shortest_directional_sequence(keypresses, 1, number_of_robots)

            if resulting_sequence_length < shortest_resulting_length:
                shortest_resulting_length = resulting_sequence_length

        sequence_length += shortest_resulting_length
        previous_key_position = current_key_position

    return sequence_length

@cache
def shortest_directional_sequence(keypresses1, current, number_of_robots):
    previous_key_position = get_key_position(dir_keypad, "A")

    sequence_length = 0

    for key in keypresses1:
        current_key_position = get_key_position(dir_keypad, key)
        possible_presses = get_possible_presses(dir_keypad, previous_key_position, current_key_position)
        previous_key_position = current_key_position

        if current == number_of_robots:
            sequence_length += len(next(iter(possible_presses)))
            continue

        shortest_resulting_length = float('inf')
        for t in possible_presses:
            resulting_sequence_length = shortest_directional_sequence(t, current + 1, number_of_robots)

            if resulting_sequence_length < shortest_resulting_length:
                shortest_resulting_length = resulting_sequence_length

        sequence_length += shortest_resulting_length

    return sequence_length

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    codes = list(data.split("\n"))

    # TODO: Might clean up later

    part1 = 0
    part2 = 0

    for code in codes:
        part1 += shortest_numeric_sequence(code, 2) * int(code[:-1])
        part2 += shortest_numeric_sequence(code, 25) * int(code[:-1])

    print("Part 1:", part1)
    print("Part 2:", part2)