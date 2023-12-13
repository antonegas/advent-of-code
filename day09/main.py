def next_seq(input):
    res = list()
    for i in range(len(input) - 1):
        res.append(input[i + 1] - input[i])
    return res

def all_zeros(input):
    for x in input:
        if x != 0:
            return False
    return True

def get_differneces(input):
    res = list()
    res.append(input)
    current = input
    while not all_zeros(current):
        current = next_seq(current)
        res.append(current)

    return res
    
def extrapulate_values(input):
    res = list()
    val = input.pop(-1)
    res.append(val[-1])
    for x in reversed(input):
        res.append(x[-1] + res[-1])

    return res

def extrapulate_values2(input):
    res = list()
    val = input.pop(-1)
    res.append(val[0])
    for x in reversed(input):
        res.append(x[0] - res[-1])

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    data = list(data.split("\n"))
    data = [list(x.split(" ")) for x in data]
    data = [[int(y) for y in x] for x in data]

    res = 0

    for x in data:
        temp = extrapulate_values2(get_differneces(x))
        res += temp[-1]

    print(res)

