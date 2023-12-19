def create_ranges(input_maps):
    res = list()
    for input_map in input_maps:
        destination, source, length = input_map
        offset = destination - source
        res.append((source, length, offset))
    return sorted(res, key=lambda x: x[0])

def create_seed_ranges1(seeds):
    res = list()
    for seed in seeds:
        res.append((seed, 1, 0))
    return sorted(res, key=lambda x: x[0])

def create_seed_ranges2(seeds):
    res = list()
    for i in range(0, len(seeds), 2):
        res.append((seeds[i], seeds[i + 1], 0))
    return sorted(res, key=lambda x: x[0])

def combine_two_ranges(from_range: tuple[int, int, int], to_range: tuple[int, int, int]):
    """ tuple[start of range, length of range, offset of range] """
    combined = list()
    from_rest = []
    to_rest = []

    if from_range[0] < to_range[0]:
        combined.append((from_range[0], min(from_range[1], to_range[0] - from_range[0]), from_range[2]))
    if from_range[0] < to_range[0] + to_range[1] and from_range[0] + from_range[1] > to_range[0]:
        combined.append((max(to_range[0], from_range[0]), min(from_range[0] + from_range[1], to_range[0] + to_range[1]) - max(from_range[0], to_range[0]), from_range[2] + to_range[2]))
    # Change rests
    if from_range[0] + from_range[1] > to_range[0] + to_range[1]:
        from_rest = [(max(to_range[0] + to_range[1], from_range[0]), min(from_range[0] + from_range[1] - to_range[0] - to_range[1], from_range[1]), from_range[2])]
    elif from_range[0] + from_range[1] < to_range[0] + to_range[1]:
        to_rest = [(max(from_range[0] + from_range[1], to_range[0]), min(to_range[0] + to_range[1] - from_range[0] - from_range[1], to_range[1]), to_range[2])]

    return combined, from_rest, to_rest


def combine_ranges(from_ranges: list[tuple[int, int, int]], to_ranges: list[tuple[int, int, int]]):
    res = list()
    current_from_ranges = from_ranges
    current_to_ranges = to_ranges
    
    while len(current_from_ranges) > 0 and len(current_to_ranges) > 0:
        next_from_range = current_from_ranges[0]
        next_to_range = current_to_ranges[0]
        to_add, rest_from, rest_to = combine_two_ranges(next_from_range, next_to_range)
        res.extend(to_add)
        current_from_ranges = rest_from + current_from_ranges[1:]
        current_to_ranges = rest_to + current_to_ranges[1:]

    res.extend(current_from_ranges)

    return sorted(res, key=lambda x: x[0])

def add_offsets(map_ranges):
    res = list()
    for map_range in map_ranges:
        start, length, offset = map_range
        res.append((start + offset, length, 0))
    return sorted(res, key=lambda x: x[0])

def location_from_seed(seed_ranges, maps):
    res = seed_ranges
    for _map in tuple(maps.values())[1:]:
        to_ranges = create_ranges(_map)
        res = add_offsets(combine_ranges(res, to_ranges))
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    data = list(list(y.strip() for y in x.split(":")) for x in data.split("\n\n"))
    maps = {x[0]: list(list(int(z) for z in y.split(" ")) for y in x[1].split("\n")) for x in data}

    seeds = maps["seeds"][0]

    print("Part 1:", min(*[x[0] for x in location_from_seed(create_seed_ranges1(seeds), maps)]))
    print("Part 2:", min(*[x[0] for x in location_from_seed(create_seed_ranges2(seeds), maps)]))