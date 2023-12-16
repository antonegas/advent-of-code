def create_ranges(input_maps):
    res = list()
    for input_map in input_maps:
        destination, source, length = input_map
        offset = source - destination
        res.append((source, length, offset))
    return sorted(res, key=lambda x: x[0])

def combine_two_ranges(range1: tuple[int, int, int], range2: tuple[int, int, int]):
    smaller, larger = (range1, range2) if range1[0] < range2[0] else (range2, range1)
    smaller_start = smaller[0]
    smaller_length = smaller[1]
    smaller_end = smaller_start + smaller_length - 1
    smaller_offset = smaller[2]
    larger_start = larger[0]
    larger_length = larger[1]
    larger_end = larger_start + larger_length - 1
    larger_offset = larger[2]

    if smaller_start == larger_start:
        if smaller_end == larger_end:
            # The ranges start and end at the same index
            return ((smaller_start, smaller_length, smaller_offset + larger_offset),)
        if smaller_end < larger_end:
            # The ranges start at the same index but the "smaller" range ends before the "larger" range
            return ((smaller_start, smaller_length, smaller_offset + larger_offset), 
                    (smaller_end + 1, larger_end - smaller_end, larger_offset))
        # The ranges start at the same index but the "smaller" range ends after the "larger" range
        return ((larger_start, larger_length, larger_offset + smaller_offset), 
                (larger_end + 1, smaller_end - larger_end, smaller_offset))
    else:
        if smaller_end == larger_end:
            # The ranges end at the same index but the "smaller" range starts before the "larger" range
            return ((smaller_start, larger_start - smaller_start, smaller_offset), 
                    (larger_start, larger_length, larger_offset + smaller_offset))
        if smaller_end < larger_end:
            # There is no overlap between the ranges.
            return ((smaller_start, smaller_length, smaller_offset), 
                    (larger_start, larger_length, larger_offset))
        # The "larger" range is contained entirely inside the "smaller" range
        return ((smaller_start, smaller_end - larger_start, smaller_offset), 
                (larger_start, larger_length, larger_offset + smaller_offset), 
                (larger_end + 1, smaller_end - larger_end, smaller_offset))


def combine_ranges(ranges_list1: list[tuple[int, int, int]], ranges_list2: list[tuple[int, int, int]]):
    res = list()
    both_ranges_lists = sorted(ranges_list1 + ranges_list2, key=lambda x: x[0])
    
    # TODO: combine ranges and add to res

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    data = list(list(y.strip() for y in x.split(":")) for x in data.split("\n\n"))
    maps = {x[0]: list(list(int(z) for z in y.split(" ")) for y in x[1].split("\n")) for x in data}

    seeds = maps["seeds"][0]