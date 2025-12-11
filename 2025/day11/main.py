from collections import defaultdict
from functools import cache

@cache
def num_paths(source, target):
    if source == target:
        return 1
    
    return sum([num_paths(x, target) for x in graph[source]])

if __name__ == "__main__":
    from os import path
    data = open(path.join(path.dirname(__file__), "input.txt"), "r").read()

    graph = defaultdict(list)
    for x, y in [[*x.split(": ")] for x in data.split("\n")]:
        graph[x] = list(y.split(" "))

    svr_to_dac = num_paths("svr", "dac")
    dac_to_fft = num_paths("dac", "fft")
    fft_to_out = num_paths("fft", "out")

    svr_to_fft = num_paths("svr", "fft")
    fft_to_dac = num_paths("fft", "dac")
    dac_to_out = num_paths("dac", "out")

    part1 = num_paths("you", "out")
    part2 = svr_to_fft * fft_to_dac * dac_to_out + svr_to_dac * dac_to_fft * fft_to_out

    print("Part 1:", part1)
    print("Part 2:", part2)