def s(start, amount):
    end = start + amount - 1
    return (start + end) * amount / 2

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    part1 = 0
    part2 = 0

    disk = list()
    current_id = 0
    free_space = list()

    for i, c in enumerate(data):
        number = int(c)
        if i % 2 == 0:
            disk.extend([current_id] * number)
            current_id += 1
        else:
            free_space.append([len(disk), number])
            disk.extend([-1] * number)

    disk1 = disk[:]

    left = 0
    right = len(disk1) - 1

    while left < right:
        if disk1[left] >= 0:
            left += 1
        elif disk1[right] < 0:
            right -= 1
        else:
            disk1[left] = disk1[right]
            disk1[right] = -1
            left += 1
            right -= 1

    disk2 = disk[:]
    moved = set()

    right = len(disk2) - 1

    while right > 0:
        current_id = disk2[right]
        right -= 1

        if current_id < 0:
            continue
        if current_id in moved:
            continue

        moved.add(current_id)

        file_size = 1

        while disk2[right] == current_id and right >= 0:
            file_size += 1
            right -= 1

        viable_free_spaces = [[i, x] for i, x in enumerate(free_space) if x[0] <= right and x[1] >= file_size]

        if len(viable_free_spaces) == 0:
            continue

        free_space_index, viable_free_space = viable_free_spaces[0]
        viable_start_index = viable_free_space[0]

        free_space[free_space_index][0] += file_size
        free_space[free_space_index][1] -= file_size

        for i in range(right + 1, right + 1 + file_size):
            disk2[i] = -1
        for i in range(viable_start_index, viable_start_index + file_size):
            disk2[i] = current_id

    print("Part 1:", sum([x * i for i, x in enumerate(disk1) if x > 0]))
    print("Part 2:", sum([x * i for i, x in enumerate(disk2) if x > 0]))