def in_bound(width, height, coord):
    x, y = coord
    return x >= 0 and y >= 0 and x <= width and y <= height

def bfs(width, height, bs, start, end):
    queue = [(start, 0)]
    explored = {start}

    while len(queue) > 0:
        coord, steps = queue.pop(0)
        if coord == end:
            return steps
        x, y = coord
        for n in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if n not in explored and in_bound(width, height, coord) and n not in bs:
                explored.add(n)
                queue.append((n, steps + 1))
    
    return -1

def binary_search(low_start, width, height, bs, start, end):
    high = len(bs)
    low = low_start
    middle = -1
    while low <= high:
        middle = (high + low) // 2
        if bfs(width, height, bs[:middle], start, end) > 0:
            low = middle + 1
        else:
            high = middle - 1
    
    return middle


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    coords = [tuple(map(int, x.split(","))) for x in data.split("\n")]

    wh = 70
    start = (0, 0)
    end = (wh, wh)
    part1_bytes = 1024
    part2_byte = coords[binary_search(part1_bytes, wh, wh, coords, start, end) - 1]

    print("Part 1:", bfs(wh, wh, coords[:part1_bytes], start, end))
    print("Part 2:", f"{part2_byte[0]},{part2_byte[1]}")