from math import prod

def transpose(matrix: list[str]) -> list[str]:
    return ["".join(x) for x in zip(*matrix)]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    *a, b = data.split("\n")

    part1 = []
    part2 = []

    t = [i for i in range(len(b)) if b[i] != " "]
    operators = [*b.split()]

    equations = [[] for _ in operators]

    for index, begin, end in zip(range(len(t)), t, t[1:] + [len(b) + 1]):
        for l in a:
            equations[index].append(l[begin:end - 1])

    for operator, equation in zip(operators, equations):
        operation = sum if operator == "+" else prod

        part1.append(operation(map(int, equation)))
        part2.append(operation(map(int, transpose(equation))))

    print("Part 1:", sum(part1))
    print("Part 2:", sum(part2))