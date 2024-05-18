def does_collide(hail1, hail2, time):
    p1, v1 = hail1
    p2, v2 = hail2

    px1, py1, pz1 = p1
    vx1, vy1, vz1 = v1
    px2, py2, pz2 = p2
    vx2, vy2, vz2 = v2

    x_diff = px1 + vx1 * time - px2 + vx2 * time
    y_diff = py1 + vy1 * time - py2 + vy2 * time
    z_diff = pz1 + vz1 * time - pz2 + vz2 * time

    return time > 0 and x_diff == y_diff == z_diff == 0


def intersection_time(hail1, hail2):
    p1, v1 = hail1
    p2, v2 = hail2

    px1, py1, pz1 = p1
    vx1, vy1, vz1 = v1
    px2, py2, pz2 = p2
    vx2, vy2, vz2 = v2

    vx_diff = vx1 - vx2
    vy_diff = vy1 - vy2
    vz_diff = vz1 - vz2
    px_diff = px1 - px2
    py_diff = py1 - py2
    pz_diff = pz1 - pz2
    
    if vx_diff != 0:
        return px_diff / vx_diff
    elif vy_diff != 0:
        return py_diff / vy_diff
    elif vz_diff != 0:
        return pz_diff / vz_diff
    else:
        return float("-inf")


def in_bound(hail, lower_bound = 7, upper_bound = 27):
    p, _ = hail
    x, y, z = p
    return lower_bound <= x <= upper_bound and lower_bound <= y <= upper_bound and lower_bound <= z <= upper_bound

def ignore_z(hail):
    p, v = hail

    px, py, _ = p
    vx, vy, _ = v
    return [[px, py, 0], [vx, vy, 0]]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    hail = [[[int(u) for u in z.split(", ")] for z in y.split(" @ ")] for y in data.split("\n")]

    print("Part 1:", sum([len([hail for hail in hail if ])]))
    print("Part 2:", 0)