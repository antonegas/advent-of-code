from collections import defaultdict

def evolve(secret_number):
    secret_number = (secret_number ^ (secret_number << 6)) & 16777215
    secret_number = (secret_number ^ (secret_number >> 5)) & 16777215
    return (secret_number ^ (secret_number << 11)) & 16777215

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    initial_secret_numbers = map(int, data.split("\n"))

    part1 = 0
    part2 = 0

    sequence_prices = defaultdict(lambda: 0)

    for initial_secret_number in initial_secret_numbers:
        seen = set()
        q = list()

        secret_number = initial_secret_number
        previous_ones = initial_secret_number % 10
        
        for _ in range(2000):
            secret_number = evolve(secret_number)

            ones_digit = secret_number % 10
            q.append(ones_digit - previous_ones)
            previous_ones = ones_digit

            if len(q) < 4:
                continue

            sequence = tuple(q)
            q.pop(0)

            if sequence in seen:
                continue

            seen.add(sequence)
            sequence_prices[sequence] += ones_digit
        
        part1 += secret_number

    print("Part 1:", part1)
    print("Part 2:", max(sequence_prices.values()))