def segment_intersection(segment1: tuple[tuple[float, float], tuple[float, float]], segment2: tuple[tuple[float, float], tuple[float, float]]) -> bool:
    u1, v1 = segment1
    u2, v2 = segment2

    xu1, yu1 = u1
    xv1, yv1 = v1
    xu2, yu2 = u2
    xv2, yv2 = v2

    if abs(yu1 - yv1) < 0.25:
        if abs(yu2 - yv2) == 0:
            return False
        if min(xu1, xv1) < xu2 < max(xu1, xv1):
            return min(yu2, yv2) < yu1 < max(yu2, yv2)
        return False
    else:
        if abs(xu2 - xv2) == 0:
            return False
        if min(yu1, yv1) < yu2 < max(yu1, yv1):
            return min(xu2, xv2) < xu1 < max(xu2, xv2)
        return False

def contains(corner1: tuple[float, float], corner2: tuple[float, float], polygon: list[tuple[float, float]]) -> bool:
    x1, y1 = corner1
    x2, y2 = corner2

    rectangle = [
        (min(x1, x2) + 0.5, min(y1, y2) + 0.5),
        (max(x1, x2) - 0.5, min(y1, y2) + 0.5),
        (max(x1, x2) - 0.5, max(y1, y2) - 0.5),
        (min(x1, x2) + 0.5, max(y1, y2) - 0.5)
    ]

    for segment1 in zip(rectangle, rectangle[1:] + [rectangle[0]]):
        for segment2 in zip(polygon, polygon[1:] + [polygon[0]]):
            if segment_intersection(segment1, segment2):
                return False

    return True

if __name__ == "__main__":
    from os import path
    data = open(path.join(path.dirname(__file__), "input.txt"), "r").read()
    points = [tuple(map(int, x.split(","))) for x in data.split("\n")]

    part1 = 0
    part2 = 0

    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

            part1 = max(part1, area)

            if contains((x1, y1), (x2, y2), points):
                part2 = max(part2, area)

    print("Part 1:", part1)
    print("Part 2:", part2)