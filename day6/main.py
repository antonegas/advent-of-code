def ways_to_win(time, distance):
    res = 0

    for pressed in range(time):
        resulting_distance = pressed * (time - pressed)
        if resulting_distance > distance:
            res += 1
    
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    data = list(list(int(y) for y in " ".join(x.split()).split(" ")[1:]) for x in data.split("\n"))
    times = data[0]
    distances = data[1]

    res1 = 1

    for i in range(len(times)):
        res1 *= ways_to_win(times[i], distances[i])

    time = ""
    for x in times:
        time += str(x)

    distance = ""
    for x in distances:
        distance += str(x)

    res2 = ways_to_win(int(time), int(distance))

    print("Part 1:", res1)
    print("Part 2:", res2)