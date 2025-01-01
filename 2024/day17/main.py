import re

def adv(registers, operand):
    registers[4] = registers[4] // (2 ** registers[operand])
    return False

def bxl(registers, operand):
    registers[5] = registers[5] ^ operand
    return False

def bst(registers, operand):
    registers[5] = registers[operand] % 8
    return False

def jnz(registers, operand):
    if registers[4] != 0:
        registers[7] = operand
        return True
    return False

def bxc(registers, operand):
    registers[5] = registers[5] ^ registers[6]
    return False

def out(registers, operand):
    registers[8].append(registers[operand] % 8)
    return False

def bdv(registers, operand):
    registers[5] = registers[4] // (2 ** registers[operand])
    return False

def cdv(registers, operand):
    registers[6] = registers[4] // (2 ** registers[operand])
    return False

def run(program, A, B, C):
    OPCODES = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    output = list()
    instruction_pointer = 0
    registers = [0, 1, 2, 3, A, B, C, instruction_pointer, output]

    while registers[7] < len(program):
        opcode = program[registers[7]]
        operand = program[registers[7] + 1]
        jumped = OPCODES[opcode](registers, operand)
        if not jumped:
            registers[7] += 2

    return output

def print_program(program):
    opcodes = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]
    is_combo = [True, False, True, False, False, True, True, True]
    combo = [0, 1, 2, 3, "A", "B", "C", "_"]
    for i in range(0, len(program), 2):
        opcode = program[i]
        operand = program[i + 1]
        if is_combo[program[i]]:
            operand = combo[program[i + 1]]
        print(f"{opcodes[opcode]} {operand}")

def print_program_math(program):
    is_combo = [True, False, True, False, False, True, True, True]
    combo = [0, 1, 2, 3, "A", "B", "C", "_"]
    for i in range(0, len(program), 2):
        opcode_index = i
        operand_index = i + 1
        opcode = program[opcode_index]
        operand = program[operand_index]
        if is_combo[opcode]:
            operand = combo[operand]
        math_strings = [
            f"A = A >> {operand}",
            f"B = B ^ {operand}",
            f"B = {operand} % 8",
            f"JUMP {operand}",
            f"B = B ^ C",
            f"OUT {operand} % 8",
            f"B = A >> {operand}",
            f"C = A >> {operand}",
        ]
        print(math_strings[opcode])

def find_possible_as(program):
    possible_as = [0]

    for current in range(len(program) - 1, -1, -1):
        new_possible_as = list()
        for possible_a in possible_as:
            shifted_possible_a = possible_a << 3
            for i in range(8):
                if run(program, shifted_possible_a + i, 0, 0) == program[current:]:
                    new_possible_as.append(shifted_possible_a + i)
        possible_as = new_possible_as

    return possible_as

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    registers_data, program_data = data.split("\n\n")
    A, B, C = [int(re.findall(r"\d+", x)[0]) for x in registers_data.split("\n")]
    program = [int(x) for x in re.findall(r"\d+", program_data)]

    print("Part 1:", ",".join(map(str, run(program, A, B, C))))
    print("Part 2:", min(find_possible_as(program)))
