UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def is_up(direction: tuple[int, int]):
    return direction[0] == UP[0] and direction[1] == UP[1]

def is_down(direction: tuple[int, int]):
    return direction[0] == DOWN[0] and direction[1] == DOWN[1]

def is_left(direction: tuple[int, int]):
    return direction[0] == LEFT[0] and direction[1] == LEFT[1]

def is_right(direction: tuple[int, int]):
    return direction[0] == RIGHT[0] and direction[1] == RIGHT[1]

def turn_into_grid(data):
    return list(data.split("\n"))

def is_loop(pipes: list[tuple[int, int]]):
    start = pipes[0]
    end = pipes[-1]
    return start[0] == end[0] and start[1] == end[1]

def find_starting_position(grid):
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == "S":
                return (x, y)


def move_along_pipes(starting_pos: tuple[int, int], direction: tuple[int, int], grid: list[str]):
    start_x = starting_pos[0]
    start_y = starting_pos[1]
    pos = (start_x + direction[0], start_y + direction[1])
    standing_on = grid[pos[1]][pos[0]]
    res = [starting_pos]

    test = len(grid)

    while True:
        res.append(pos)

        if pos[0] == -1 or pos[0] == len(grid[0]) or pos[1] == -1 or pos[1] == len(grid):
            break

        if standing_on == "S" or standing_on == ".":
            break

        elif standing_on == "|":
            if not is_up(direction) and not is_down(direction):
                break

        elif standing_on == "-":
            if not is_left(direction) and not is_right(direction):
                break

        elif standing_on == "L":
            if is_down(direction):
                direction = RIGHT
            elif is_left(direction):
                direction = UP
            else:
                break
        
        elif standing_on == "J":
            if is_down(direction):
                direction = LEFT
            elif is_right(direction):
                direction = UP
            else:
                break

        elif standing_on == "7":
            if is_up(direction):
                direction = LEFT
            elif is_right(direction):
                direction = DOWN
            else:
                break

        elif standing_on == "F":
            if is_up(direction):
                direction = RIGHT
            elif is_left(direction):
                direction = DOWN
            else:
                break

        pos = (pos[0] + direction[0], pos[1] + direction[1])
        standing_on = grid[pos[1]][pos[0]]

    return res

def find_loop(grid):
    starting_pos = find_starting_position(grid)
    res = move_along_pipes(starting_pos, DOWN, grid)

    if is_loop(res):
        return res
    
    res = move_along_pipes(starting_pos, LEFT, grid)
    
    if is_loop(res):
        return res
    
    res = move_along_pipes(starting_pos, RIGHT, grid)
    
    if is_loop(res):
        return res
    
    res = move_along_pipes(starting_pos, UP, grid)
    
    if is_loop(res):
        return res
    
def furthest_point(loop):
    return (len(loop) - 1) // 2

def calculate_area(loop):
    """ 
    Gauss' shoelace formula: https://gamedev.stackexchange.com/a/151036
    """
    area = 0

    for i in range(len(loop)):
        area += loop[i][0] * loop[(i + 1) % len(loop)][1] - loop[i][1] * loop[(i + 1) % len(loop)][0]

    return area // 2

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    grid: list[str] = turn_into_grid(data)

    loop = find_loop(grid)

    print("Part 1:", furthest_point(loop))
    # Area of loop has to be removed as it is included in calculated area
    print("Part 2:", abs(calculate_area(loop)) - furthest_point(loop) + 1)