from math import lcm

def into_dict(graph):
    res = dict()
    data = list(graph.split("\n"))
    for x in data:
        LR = dict()
        LR["L"] = x[7:10]
        LR["R"] = x[12:15]
        res[x[0:3]] = LR
    return res

def steps_required(navigation_instructions, graph):
    res = 0
    nodes = into_dict(graph)
    current = "AAA"

    while True:
        for lr in navigation_instructions:
            res += 1
            current = nodes[current][lr]
            if current == "ZZZ":
                break
        if current == "ZZZ":
            return res
        
def ghost_steps_required(navigation_instructions, graph):
    res = list()
    nodes = into_dict(graph)
    start_nodes = get_ghost_nodes(nodes)

    for start_node in start_nodes:
        steps = 0
        current = start_node
        while True:
            for lr in navigation_instructions:
                steps += 1
                current = nodes[current][lr]
                if current[-1] == "Z":
                    break
            if current[-1] == "Z":
                res.append(steps)
                break

    return lcm(*res)

def get_ghost_nodes(nodes):
    res = list()
    for node in nodes.keys():
        if node[-1] == "A":
            res.append(node)
    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    navigation_instructions, nodes = data.split("\n\n")
            
    print("Part 1:", steps_required(navigation_instructions, nodes))
    print("Part 2:", ghost_steps_required(navigation_instructions, nodes))

