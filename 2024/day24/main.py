import re
from math import log2, floor

def print_graphviz(gates):
    for input1, operation, input2, output in gates:
        print(f"{input1} -> {output} [ label=\"{operation}\" ]")
        print(f"{input2} -> {output} [ label=\"{operation}\" ]")

def simulate(initial_wires, gates):
    wires = dict(initial_wires)
    remaining_gates = gates[:]

    OPERATIONS = {
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "XOR": lambda a, b: a ^ b
    }

    while remaining_gates:
        for index in range(len(remaining_gates)):
            input1, operation, input2, output = remaining_gates[index]
            if input1 not in wires or input2 not in wires:
                continue
            wires[output] = OPERATIONS[operation](wires[input1], wires[input2])
            remaining_gates.pop(index)
            break

    return wires

def swap_wires(gates, wire1, wire2):
    outputs = [gate[3] for gate in gates]
    wire_index1 = outputs.index(wire1)
    wire_index2 = outputs.index(wire2)
    gates[wire_index1] = gates[wire_index1][:3] + (wire2,)
    gates[wire_index2] = gates[wire_index2][:3] + (wire1,)

def get_z_wires(wires):
    return [z for z in wires if z[0] == "z"]

def get_z_decimal(wires):
    char_wires = get_z_wires(wires)
    char_binary = ""

    for char_wire in reversed(sorted(char_wires)):
        char_binary += str(wires[char_wire])

    return int(char_binary, 2)

def create_initial(x, y):
    initial_wires = dict()

    for x_wire, x_value in enumerate(reversed(bin(x)[2:].zfill(45))):
        initial_wires[f"x{str(x_wire).zfill(2)}"] = int(x_value)
    for y_wire, y_value in enumerate(reversed(bin(y)[2:].zfill(45))):
        initial_wires[f"y{str(y_wire).zfill(2)}"] = int(y_value)

    return initial_wires

def find_first_wrong(gates, start=0):
    for bit in range(start, 45):
        expected = 2**(bit + 1) - 2
        initial_wires = create_initial(2**bit - 1, 2**bit - 1)
        actual = get_z_decimal(simulate(initial_wires, gates))
        if expected != actual:
            diff = expected ^ actual
            return floor(log2(diff & -diff))

    return -1

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    wires_data, gates_data = data.split("\n\n")

    initial_wires = {wire: int(boolean) for wire, boolean in [tuple(x.split(": ")) for x in wires_data.split("\n")]}
    gates = [tuple(re.split(r"\W+", x)) for x in gates_data.split("\n")]

    part1 = 0
    part2 = 0

    swaps = [
        ("bpf", "z05"),
        ("hcc", "z11"),
        ("hqc", "qcw"),
        ("z35", "fdw"),
    ]

    for wire1, wire2 in swaps:
        swap_wires(gates, wire1, wire2)

    # swap_wires(gates, "bpf", "z05")
    # swap_wires(gates, "hcc", "z11")
    # swap_wires(gates, "hqc", "qcw")
    # swap_wires(gates, "z35", "fdw")
    print(find_first_wrong(gates, 0))

    print("Part 1:", get_z_decimal(simulate(initial_wires, gates)))
    print("Part 2:", ",".join(sorted([x for xs in swaps for x in xs])))