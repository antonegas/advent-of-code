def get_coordinates1(dig_plan):
    res = [(0, 0)]
    for dig_directions in dig_plan[:-1]:
        direction, distance, _ = dig_directions
        if direction == "U":
            res.append((res[-1][0], res[-1][1] - distance ))
        elif direction == "D":
            res.append((res[-1][0], res[-1][1] + distance ))
        elif direction == "L":
            res.append((res[-1][0] - distance , res[-1][1]))
        elif direction == "R":
            res.append((res[-1][0] + distance , res[-1][1]))
    return res

def get_coordinates2(dig_plan):
    res = [(0, 0)]
    for dig_directions in dig_plan[:-1]:
        direction = int(dig_directions[2][-1])
        distance = int(dig_directions[2][:-1], 16)
        if direction == 3:
            # Up
            res.append((res[-1][0], res[-1][1] - distance ))
        elif direction == 1:
            # Down
            res.append((res[-1][0], res[-1][1] + distance ))
        elif direction == 2:
            # Left
            res.append((res[-1][0] - distance , res[-1][1]))
        elif direction == 0:
            # Right
            res.append((res[-1][0] + distance , res[-1][1]))
    return res

def calculate_area(dig_plan, hex_directions):
    """ 
    Gauss' shoelace formula: https://gamedev.stackexchange.com/a/151036
    """
    area = 0
    coordinates = get_coordinates2(dig_plan) if hex_directions else get_coordinates1(dig_plan)
    outer_area =  sum([int(x[2][:-1], 16) for x in dig_plan]) if hex_directions else sum([x[1] for x in dig_plan])

    for i in range(len(coordinates)):
        area += coordinates[i][0] * coordinates[(i + 1) % len(coordinates)][1] - coordinates[i][1] * coordinates[(i + 1) % len(coordinates)][0]

    return (abs(area) + outer_area) // 2 + 1

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    dig_plan = list((y[0], int(y[1]), y[2][2:-1]) for y in list(tuple(x.split(" ")) for x in data.split("\n")))

    print("Part 1:", calculate_area(dig_plan, False))
    print("Part 2:", calculate_area(dig_plan, True))