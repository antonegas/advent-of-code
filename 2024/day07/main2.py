def dfs(current, equation, operations):
    if len(equation) == 1:
        return equation[0] == current
    for operation in operations:
        possible, next_value = operation(current, equation[-1])
        if possible and dfs(next_value, equation[:-1], operations):
            return True
    return False

def subract(a, b):
    return b < a, a - b

def divide(a, b):
    return a % b == 0, a // b

def seperate(a, b):
    if len(str(a)) <= len(str(b)):
        return False, 0
    return str(a)[-len(str(b)):] == str(b), int(str(a)[:-len(str(b))])

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    equations_data = [tuple(x.split(": ")) for x in data.split("\n")]
    equations = [(int(value), tuple(map(int, equation.split(" ")))) for value, equation in equations_data]

    # Operations are done in reverse to determine if a eqation NOT possible quicker
    operations = [subract, divide, seperate]

    print("Part 1:", sum([value for value, equation in equations if dfs(value, equation, operations[:2])]))
    print("Part 2:", sum([value for value, equation in equations if dfs(value, equation, operations)]))