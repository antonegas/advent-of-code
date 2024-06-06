
from itertools import combinations

def path_intersection_time(hail1, hail2):
    p1, v1 = hail1
    p2, v2 = hail2

    px1, py1, _ = p1
    vx1, vy1, _ = v1
    px2, py2, _ = p2
    vx2, vy2, _ = v2

    A = vx1
    B = -vx2
    C = vy1
    D = -vy2
    x = px2 - px1
    y = py2 - py1

    determinant = A * D - B * C

    if determinant == 0:
        return [float("-inf"), float("-inf")]
    else:
        return [
            (D * x - B * y) / determinant,
            (A * y - C * x) / determinant
        ]
    

def hail_at_time(hail, nano_seconds):
    p, v = hail
    px, py, pz = p
    vx, vy, vz = v
    position_at_time = [
        px + vx * nano_seconds,
        py + vy * nano_seconds,
        pz + vz * nano_seconds
    ]
    return [position_at_time, v]


def ignore_z(hail):
    p, v = hail

    px, py, _ = p
    vx, vy, _ = v
    return [[px, py, 0], [vx, vy, 0]]


def in_bound(hail, x_bound, y_bound, z_bound):
    x_min, x_max = x_bound
    y_min, y_max = y_bound
    z_min, z_max = z_bound
    x, y, z = hail[0]
    
    return x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max 
    

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    hail = [[[int(u) for u in z.split(", ")] for z in y.split(" @ ")] for y in data.split("\n")]

    print("Part 1:", sum([len(list(0 for hail1, t1, t2 in list([hail1] + path_intersection_time(hail1, hail2) for hail2 in [ignore_z(_hail) for _hail in hail[i + 1:]]) if t1 >= 0 and t2 >= 0 and in_bound(hail_at_time(hail1, t1), [2e14, 2e14], [2e14, 2e14], [0, 0]))) for i, hail1 in enumerate([ignore_z(_hail) for _hail in hail])]))
    # print("Part 2:", 0)