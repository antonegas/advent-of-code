from collections import defaultdict


def is_overlapping(brick1, brick2):
    return ((brick2[0][0] <= brick1[0][0] <= brick2[1][0] or 
            brick2[0][0] <= brick1[1][0] <= brick2[1][0] or
            brick1[0][0] <= brick2[0][0] <= brick1[1][0] or 
            brick1[0][0] <= brick2[1][0] <= brick1[1][0]) and 
            (brick2[0][1] <= brick1[0][1] <= brick2[1][1] or 
            brick2[0][1] <= brick1[1][1] <= brick2[1][1] or
            brick1[0][1] <= brick2[0][1] <= brick1[1][1] or 
            brick1[0][1] <= brick2[1][1] <= brick1[1][1]))

def get_overlapping(brick, bricks):
    return list(_brick for _brick in bricks if is_overlapping(brick, _brick))

def fall(brick, landed_bricks):
    overlapping_bricks = get_overlapping(brick, sorted(landed_bricks, key=lambda x: x[1][2]))
    highest_overlapping_point = overlapping_bricks[-1][1][2] + 1 if overlapping_bricks else 0
    diff = brick[0][2] - highest_overlapping_point
    landed_brick = ((brick[0][0], brick[0][1], highest_overlapping_point), 
                    (brick[1][0], brick[1][1], brick[1][2] - diff))
    supported_by = [_brick for _brick in overlapping_bricks if _brick[1][2] == (highest_overlapping_point - 1)]
    return landed_brick, supported_by

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    bricks = sorted(list((tuple(int(z1) for z1 in y1.split(",")), tuple(int(z2) for z2 in y2.split(","))) for y1, y2 in list(x.split("~") for x in data.split("\n"))), key=lambda x: x[0][2])

    landed_bricks = list()
    supported_by = dict()
    supporting = defaultdict(lambda: list())

    for brick in bricks:
        landed_brick, supporting_bricks = fall(brick, landed_bricks)
        landed_bricks.append(landed_brick)
        supported_by[brick] = supporting_bricks
        for supporting_brick in supporting_bricks:
            supporting[supporting_brick].append(brick)

    print("Part 1:", len(bricks) - len(set(supporting_bricks[0] for supporting_bricks in supported_by.values() if len(supporting_bricks) == 1)))
    print("Part 2:", 0)