from functools import cache
from collections import defaultdict, deque

@cache
def evolve(secret_number):
    t1 = (secret_number ^ (secret_number << 6)) & 16777215
    t2 = (t1 ^ (t1 >> 5)) & 16777215
    return (t2 ^ (t2 << 11)) & 16777215

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    initial_secret_numbers = map(int, data.split("\n"))

    part1 = 0
    part2 = 0

    best = 0
    current = defaultdict(lambda: 0)

    for initial_secret_number in initial_secret_numbers:
        secret_number = initial_secret_number
        seen = set()
        q = deque()
        previous_ones = initial_secret_number % 10
        for _ in range(2000):
            secret_number = evolve(secret_number)
            ones_digit = secret_number % 10
            q.append(ones_digit - previous_ones)
            previous_ones = ones_digit
            if len(q) < 4:
                continue
            key = tuple(q)
            q.popleft()
            if key in seen:
                continue
            seen.add(key)
            current[key] += ones_digit
            if current[key] > best:
                best = current[key]
                best_seq = key
        
        part1 += secret_number

    print("Part 1:", part1)
    print("Part 2:", best)