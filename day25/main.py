from collections import defaultdict
from random import sample
from copy import deepcopy
from math import prod

def get_graph(wiring_diagram):
    res = defaultdict(lambda: set())

    for key_component, connected_components in wiring_diagram.items():
        for connected_component in connected_components:
            res[key_component].add(connected_component)
            res[connected_component].add(key_component)

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
    wiring_graph = remove_cuts(wiring_graph, cuts)
    first_cut = cuts[0]

    return get_group_size(wiring_graph, first_cut[0]), get_group_size(wiring_graph, first_cut[1])

def get_cuts(wiring_graph, deterministic=False):
    if deterministic:
        return stoer_wagner(wiring_graph)
    else:
        return monte_carlo(wiring_graph)
    

def remove_cut(wiring_graph, cut):
    res = deepcopy(wiring_graph)
    component1, component2 = cut

    res[component1].discard(component2)
    res[component2].discard(component1)

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
    pass


if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    wiring_diagram = {k: list(v.split()) for k, v in [x.split(":") for x in data.split("\n")]}

    # wiring_graph = get_graph(wiring_diagram)

    # wiring_graph = remove_cut(wiring_graph, ("hfx", "pzl"))
    # wiring_graph = remove_cut(wiring_graph, ("bvb", "cmg"))
    # wiring_graph = remove_cut(wiring_graph, ("nvd", "jqt"))

    print("Part 1:", prod(get_group_sizes(wiring_diagram, deterministic=False)))
    print("Part 2:", 0)