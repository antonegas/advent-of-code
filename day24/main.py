
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
    

def total_intersections(hail, bounds = (2e14, 4e14)):
    res = 0

    for hail1, hail2 in combinations([ignore_z(_hail) for _hail in hail], 2):
        t1, t2 = path_intersection_time(hail1, hail2)
        moved_hail1 = hail_at_time(hail1, t1)
        if in_bound(moved_hail1, bounds, bounds, (0, 0)) and t1 >= 0 and t2 >= 0:
            res += 1

    return res
    

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


def perfect_throw(hail):
    matrix, y = get_equation_matrix(hail)
    hail1, hail2, *_ = hail
    
    p1, v1 = hail1
    p2, v2 = hail2

    px1, _, pz1 = p1
    vx1, _, vz1 = v1
    px2, _, pz2 = p2
    vx2, _, vz2 = v2

    det = determinant4x4(matrix)
    pxr = x1(matrix, y, det)
    pyr = x2(matrix, y, det)
    vxr = x3(matrix, y, det)
    vyr = x4(matrix, y, det)

    t1 = (pxr - px1) // (vx1 - vxr)
    t2 = (pxr - px2) // (vx2 - vxr)

    vzr = (pz1 - pz2 + t1 * vz1 - t2 * vz2) // (t1 - t2)
    pzr = pz1 + t1 * (vz1 - vzr)

    return [[pxr, pyr, pzr], [vxr, vyr, vzr]]


def get_equation_matrix(hail):
    hail0, hail1, hail2, hail3, hail4, hail5, hail6, hail7, *_ = hail

    p0, v0 = hail0
    p1, v1 = hail1
    p2, v2 = hail2
    p3, v3 = hail3
    p4, v4 = hail4
    p5, v5 = hail5
    p6, v6 = hail6
    p7, v7 = hail7

    px0, py0, _ = p0
    vx0, vy0, _ = v0
    px1, py1, _ = p1
    vx1, vy1, _ = v1
    px2, py2, _ = p2
    vx2, vy2, _ = v2
    px3, py3, _ = p3
    vx3, vy3, _ = v3
    px4, py4, _ = p4
    vx4, vy4, _ = v4
    px5, py5, _ = p5
    vx5, vy5, _ = v5
    px6, py6, _ = p6
    vx6, vy6, _ = v6
    px7, py7, _ = p7
    vx7, vy7, _ = v7

    matrix = [
        [vy0 - vy1, vx1 - vx0, py1 - py0, px0 - px1],
        [vy2 - vy3, vx3 - vx2, py3 - py2, px2 - px3],
        [vy4 - vy5, vx5 - vx4, py5 - py4, px4 - px5],
        [vy6 - vy7, vx7 - vx6, py7 - py6, px6 - px7]
    ]

    y = [
        px0 * vy0 - py0 * vx0 + py1 * vx1 - px1 * vy1,
        px2 * vy2 - py2 * vx2 + py3 * vx3 - px3 * vy3,
        px4 * vy4 - py4 * vx4 + py5 * vx5 - px5 * vy5,
        px6 * vy6 - py6 * vx6 + py7 * vx7 - px7 * vy7
    ]

    return matrix, y


def determinant4x4(matrix):
    a, b, c, d = matrix
    a1, a2, a3, a4 = a
    b1, b2, b3, b4 = b
    c1, c2, c3, c4 = c
    d1, d2, d3, d4 = d

    return a2 * b4 * c3 * d1 - a2 * b3 * c4 * d1 - a1 * b4 * c3 * d2 + a1 * b3 * c4 * d2 - a2 * b4 * c1 * d3 + a1 * b4 * c2 * d3 + a2 * b1 * c4 * d3 - a1 * b2 * c4 * d3 + a4 * (b3 * (c2 * d1 - c1 * d2) + b2 * (c1 * d3 - c3 * d1) + b1 * (c3 * d2 - c2 * d3)) + a2 * b3 * c1 * d4 - a1 * b3 * c2 * d4 - a2 * b1 * c3 * d4 + a1 * b2 * c3 * d4 + a3 * (b4 * (c1 * d2 - c2 * d1) + b2 * (c4 * d1 - c1 * d4) + b1 * (c2 * d4 - c4 * d2))


def x1(matrix, y, det):
    a, b, c, d = matrix
    _, a2, a3, a4 = a
    _, b2, b3, b4 = b
    _, c2, c3, c4 = c
    _, d2, d3, d4 = d
    y1, y2, y3, y4 = y

    matrix1 = [
        [y1, a2, a3, a4],
        [y2, b2, b3, b4],
        [y3, c2, c3, c4],
        [y4, d2, d3, d4]
    ]

    return determinant4x4(matrix1) // det


def x2(matrix, y, det):
    a, b, c, d = matrix
    a1, _, a3, a4 = a
    b1, _, b3, b4 = b
    c1, _, c3, c4 = c
    d1, _, d3, d4 = d
    y1, y2, y3, y4 = y

    matrix2 = [
        [a1, y1, a3, a4],
        [b1, y2, b3, b4],
        [c1, y3, c3, c4],
        [d1, y4, d3, d4]
    ]

    return determinant4x4(matrix2) // det


def x3(matrix, y, det):
    a, b, c, d = matrix
    a1, a2, _, a4 = a
    b1, b2, _, b4 = b
    c1, c2, _, c4 = c
    d1, d2, _, d4 = d
    y1, y2, y3, y4 = y

    matrix3 = [
        [a1, a2, y1, a4],
        [b1, b2, y2, b4],
        [c1, c2, y3, c4],
        [d1, d2, y4, d4]
    ]

    return determinant4x4(matrix3) // det


def x4(matrix, y, det):
    a, b, c, d = matrix
    a1, a2, a3, _ = a
    b1, b2, b3, _ = b
    c1, c2, c3, _ = c
    d1, d2, d3, _ = d
    y1, y2, y3, y4 = y

    matrix4 = [
        [a1, a2, a3, y1],
        [b1, b2, b3, y2],
        [c1, c2, c3, y3],
        [d1, d2, d3, y4]
    ]

    return determinant4x4(matrix4) // det


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    hail = [[[int(u) for u in z.split(", ")] for z in y.split(" @ ")] for y in data.split("\n")]  

    print("Part 1:", total_intersections(hail))
    print("Part 2:", sum(perfect_throw(hail)[0]))