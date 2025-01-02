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

def find_first_wrong(gates):
    for bit in range(45):
        expected = 2**(bit + 1) - 2
        initial_wires = create_initial(2**bit - 1, 2**bit - 1)
        actual = get_z_decimal(simulate(initial_wires, gates))
        if expected != actual:
            diff = expected ^ actual
            return floor(log2(diff & -diff))

    return -1

def fix_gates(gates):
    swaps = list()
    
    # AND1 and XOR2 swapped
    gate3_xor2 = find_gates(gates, input1=r"x\d\d", operation="AND", input2=r"y\d\d", output=r"z\d\d")[0]
    gate3_xor1 = find_gates(gates, input1=gate3_xor2[0], operation="XOR")[0]
    gate3_and1 = find_gates(gates, input1=gate3_xor1[3], operation="XOR")[0]
    swaps.append((gate3_and1[3], gate3_xor2[3]))

    # AND2 and XOR2 swapped
    gate8_xor2 = find_gates(gates, input1=r"(?!([xy]\d\d))\w{3}", operation="AND", output=r"z\d\d")[0]
    gate8_and2 = find_gates(gates, input1=gate8_xor2[0], operation="XOR")[0]
    swaps.append((gate8_and2[3], gate8_xor2[3]))

    # OR and XOR2 swapped
    gate10_xor2 = find_gates(gates, operation="OR", output=r"z(?!45)\d\d")[0]
    gate10_and2 = find_gates(gates, input1=f"x{gate10_xor2[3][1:]}", operation="XOR")[0]
    gate10_or = find_gates(gates, input1=gate10_and2[3], operation="XOR")[0]
    swaps.append((gate10_or[3], gate10_xor2[3]))

    semi_fixed_gates = gates[:]

    for wire1, wire2 in swaps:
        swap_wires(semi_fixed_gates, wire1, wire2)

    # AND1 and XOR1 swapped
    gate1_index = find_first_wrong(semi_fixed_gates)
    gate1_and1 = find_gates(gates, input1=f"x{gate1_index}", operation="AND", input2=f"y{gate1_index}")[0]
    gate1_xor1 = find_gates(gates, input1=f"x{gate1_index}", operation="XOR", input2=f"y{gate1_index}")[0]
    swaps.append((gate1_and1[3], gate1_xor1[3]))

    return swaps

def find_gates(gates, input1 = r"\w{3}", input2 = r"\w{3}", operation = r"(AND|OR|XOR)", output = r"\w{3}"):
    pattern = f"({input1} {operation} {input2}|{input2} {operation} {input1}) -> {output}"
    return [gate for gate in gates if re.match(pattern, f"{gate[0]} {gate[1]} {gate[2]} -> {gate[3]}")]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    wires_data, gates_data = data.split("\n\n")

    initial_wires = {wire: int(boolean) for wire, boolean in [tuple(x.split(": ")) for x in wires_data.split("\n")]}
    gates = [tuple(re.findall(r"\w+", x)) for x in gates_data.split("\n")]

    part1 = 0
    part2 = 0

    swaps = fix_gates(gates)

    print("Part 1:", get_z_decimal(simulate(initial_wires, gates)))
    print("Part 2:", ",".join(sorted([x for xs in swaps for x in xs])))