MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
RED = "red"
GREEN = "green"
BLUE = "blue"

def possible(game):
    for subset in game:
        for cubes in subset:
            amount = int(cubes[0])
            color = cubes[1]
            if color == RED and amount > MAX_RED:
                return False
            elif color == GREEN and amount > MAX_GREEN:
                return False
            elif color == BLUE and amount > MAX_BLUE:
                return False
    
    return True

def smallest_and_possible(game):
    smallest_red = 0
    smallest_green = 0
    smallest_blue = 0

    for subset in game:
        for cubes in subset:
            amount = int(cubes[0])
            color = cubes[1]
            if color == RED and amount > smallest_red:
                smallest_red = amount
            elif color == GREEN and amount > smallest_green:
                smallest_green = amount
            elif color == BLUE and amount > smallest_blue:
                smallest_blue = amount

    return (smallest_red, smallest_green, smallest_blue)

def game_power(game):
    r, g, b = smallest_and_possible(game)
    return r * g * b

if __name__ == "__main__":
    import os
    import re
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    games = list(list(list(tuple(z.split(" ")) for z in y.split(", ")) for y in x.split(": ")[1].split("; ")) for x in data.split("\n"))

    print("Part 1:", sum([i + 1 for i, game in enumerate(games) if possible(game)]))
    print("Part 2:", sum([game_power(game) for game in games]))