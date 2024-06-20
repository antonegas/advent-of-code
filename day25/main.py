from collections import defaultdict
from random import sample
from copy import deepcopy
from math import prod

def get_graph(wiring_diagram):
    res = defaultdict(lambda: dict())

    for key_component, connected_components in wiring_diagram.items():
        for connected_component in connected_components:
            # res[key_component][connected_component] = 1
            # res[connected_component][key_component] = 1
            res[(key_component,)][(connected_component,)] = 1
            res[(connected_component,)][(key_component,)] = 1

    return res

def get_group_size(wiring_graph, start):
    queue = list()
    explored = set()

    queue.append(start)
    explored.add(start)

    while queue:
        current = queue.pop(0)
        for connected in wiring_graph[current]:
            if connected not in explored:
                explored.add(connected)
                queue.append(connected)

    return len(explored)

def get_group_sizes(wiring_diagram, deterministic=False):
    wiring_graph = get_graph(wiring_diagram)
    cuts = get_cuts(wiring_graph, deterministic)
    first_cut = cuts[0]
    wiring_graph = remove_cuts(wiring_graph, cuts)

    return get_group_size(wiring_graph, first_cut[0]), get_group_size(wiring_graph, first_cut[1])

def get_cuts(wiring_graph, deterministic=False):
    if deterministic:
        return stoer_wagner(wiring_graph)
    else:
        return monte_carlo(wiring_graph)

def remove_cut(wiring_graph, cut):
    res = deepcopy(wiring_graph)
    component1, component2 = cut

    res[component1].pop(component2)
    res[component2].pop(component1)

    return res

def remove_cuts(wiring_graph, cuts):
    res = wiring_graph

    for cut in cuts:
        res = remove_cut(res, cut)

    return res

def monte_carlo(wiring_graph):
    uses = defaultdict(lambda: 0)

    while True:
        for _ in range(10):
            start, end = sample(list(wiring_graph.keys()), 2)
            path = get_path(wiring_graph, start, end)

            for i in range(len(path) - 1):
                node1 = path[i]
                node2 = path[i + 1]
                edge = tuple(sorted([node1, node2]))
                uses[edge] += 1

        possible_cuts = sorted(uses.keys(), key=lambda x: uses[x])[-3:]
        first_cut = possible_cuts[0]

        cut_wiring_graph = remove_cuts(wiring_graph, possible_cuts)
        group1_size = get_group_size(cut_wiring_graph, first_cut[0])
        group2_size = get_group_size(cut_wiring_graph, first_cut[1])

        if group1_size + group2_size == len(wiring_graph):
            break

    return sorted(uses.keys(), key=lambda x: uses[x])[-3:]

def get_path(wiring_graph, start, end):
    queue = list()
    explored = set()
    parent = dict()

    queue.append(start)
    explored.add(start)

    while queue:
        current = queue.pop(0)

        if current == end:
            break

        for connected in wiring_graph[current]:
            if connected not in explored:
                explored.add(connected)
                parent[connected] = current
                queue.append(connected)

    path = list()
    current = end
    path.append(end)

    while current != start:
        current = parent[current]
        path.append(current)

    return path

def stoer_wagner(wiring_graph):
    merged_nodes = defaultdict(lambda: set())
    current_wiring_graph = wiring_graph
    current_best_cut = ()
    current_best_cost = float("inf")

    while len(current_wiring_graph) > 1:
        cut, cost = minimum_cut_phase(current_wiring_graph, merged_nodes)
        if cost < current_best_cost:
            current_best_cut = cut
            current_best_cost = cost
    
    return current_best_cut

def minimum_cut_phase(wiring_graph, merged_nodes):
    start = next(iter(wiring_graph))
    A = {start}
    last_added = start

    while A != wiring_graph.keys():
        A.add(most_tightly_connected(wiring_graph, A))

def cut_of_the_phase(wiring_graph, A):
    pass

def most_tightly_connected(wiring_graph, checked):
    connected = get_connected(wiring_graph, checked)

    return max(connected, key=lambda x: connected[x])

def get_connected(wiring_graph, merged):
    connected = defaultdict(lambda: 0)

    for key in merged:
        for connection in wiring_graph[key]:
            if connection not in merged:
                connected[connection] += wiring_graph[connection]

    return connected

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    wiring_diagram = {k: list(v.split()) for k, v in [x.split(":") for x in data.split("\n")]}

    print("Part 1:", prod(get_group_sizes(wiring_diagram, deterministic=False)))
    print("Part 2:", 0)