from math import lcm

def init_state(machine):
    res = dict()

    for module in machine:
        value = machine[module]
        if is_flip_flop(machine, module):
            # current
            res[module] = "LOW"
        elif is_conjunction(machine, module):
            # last received
            res[module] = {k: "LOW" for k in [_module for _module in machine if not is_broadcaster(machine, _module) and module in machine[_module][1]]}

    return res

def is_broadcaster(machine, module):
    return machine[module][0] not in "%&"

def is_flip_flop(machine, module):
    return machine[module][0] == "%"

def is_conjunction(machine, module):
    return machine[module][0] == "&"
    
def broadcast(machine):
    return [(module, "broadcaster", "LOW") for module in machine["broadcaster"]]

def flip_flop(machine, state, module, pulse):
    sends_to_modules = machine[module][1]
    current = state[module]
    if pulse == "HIGH":
        return list()
    state[module]= "HIGH" if current == "LOW" else "LOW"
    return [(_module, module, state[module]) for _module in sends_to_modules]

def conjunction(machine, state, module_to, module_from, pulse):
    sends_to_modules = machine[module_to][1]
    state[module_to][module_from] = pulse
    last_received = state[module_to]
    pulse = "HIGH" if "LOW" in last_received.values() else "LOW" 
    return [(_module, module_to, pulse) for _module in sends_to_modules]

def increase_counts(counts, pulse):
    return (counts[0] + (pulse == "LOW"), counts[1] + (pulse == "HIGH"))

def press_button(machine, number_of_presses):
    state = init_state(machine)
    counts = (0, 0) # LOW, HIGH
    presses = 0

    while presses < number_of_presses: 
        presses += 1
        queue = [("broadcaster", "button", "LOW")]
        while queue:
            module_to, module_from, pulse = queue.pop(0)
            counts = increase_counts(counts, pulse)

            if module_to not in machine:
                continue

            if is_broadcaster(machine, module_to):
                queue.extend(broadcast(machine))
            elif is_conjunction(machine, module_to):
                queue.extend(conjunction(machine, state, module_to, module_from, pulse))
            elif is_flip_flop(machine, module_to):
                queue.extend(flip_flop(machine, state, module_to, pulse))
    
    return counts[0] * counts[1]

def get_binary_counters(machine):
    res = list()

    for counter_start in machine["broadcaster"]:
        counter_next = ""
        counter_end = ""
        for module in machine[counter_start][1]:
            if is_conjunction(machine, module):
                counter_end = module
            else:
                counter_next = module
        res.append((counter_end, counter_next))
        
    return res

def get_counter_number(machine, counter):
    res = "1"
    counter_end, counter_next = counter

    while True:
        if len(machine[counter_next][1]) == 2:
            res = "1" + res
            counter_next = [module for module in machine[counter_next][1] if module != counter_end][0]
        elif machine[counter_next][1][0] == counter_end:
            return int("1" + res, 2)
        else:
            res = "0" + res
            counter_next = machine[counter_next][1][0]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    machine = {(y[0] if y[0] == "broadcaster" else y[0][1:]): (y[1:] if y[0] == "broadcaster" else (y[0][0], y[1:])) for y in tuple((first,) + tuple(second.split(", ")) for first, second in list(list(x.split(" -> ")) for x in list(data.split("\n"))))}

    print("Part 1:", press_button(machine, 1000))
    print("Part 2:", lcm(*[get_counter_number(machine, counter) for counter in get_binary_counters(machine)]))