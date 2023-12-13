def from_x_to_mapping(from_x, mapping):
    for to in mapping:
        start_from = to[1]
        end_from = start_from + to[2]
        start_to = to[0]

        if from_x in range(start_from, end_from):
            diff = from_x - start_from
            return start_to + diff
    
    return from_x

def from_seed_to_location(seed, maps):
    soil = from_x_to_mapping(seed, maps["seed-to-soil map"])
    fertilizer = from_x_to_mapping(soil, maps["soil-to-fertilizer map"])
    water = from_x_to_mapping(fertilizer, maps["fertilizer-to-water map"])
    light = from_x_to_mapping(water, maps["water-to-light map"])
    tempeture = from_x_to_mapping(light, maps["light-to-temperature map"])
    humidity = from_x_to_mapping(tempeture, maps["temperature-to-humidity map"])
    location = from_x_to_mapping(humidity, maps["humidity-to-location map"])
    return location

def seed2_generator(seeds):
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = start + seeds[i + 1]
        for seed in range(start, end):
            yield seed

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    data = list(list(y.strip() for y in x.split(":")) for x in data.split("\n\n"))
    maps = {x[0]: list(list(int(z) for z in y.split(" ")) for y in x[1].split("\n")) for x in data}
    
    seeds = maps["seeds"][0]

    print("Part 1:", min(list(from_seed_to_location(seed, maps) for seed in seeds)))
    print("Part 2:", min(list(from_seed_to_location(seed, maps) for seed in seed2_generator(seeds))))