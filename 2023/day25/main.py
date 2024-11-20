from collections import defaultdict
from random import sample
from copy import deepcopy
from math import prod

def get_graph(wiring_diagram):
    res = defaultdict(lambda: defaultdict(lambda: 0))

    for key_component, connected_components in wiring_diagram.items():
        for connected_component in connected_components:
            res[key_component][connected_component] = 1
            res[connected_component][key_component] = 1

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
    current_best_cut = set()
    current_best_cost = float("inf")

    while len(current_wiring_graph) > 1:
        current_wiring_graph, merged_nodes, A = minimum_cut_phase(current_wiring_graph, merged_nodes)
        cut, cost = cut_of_the_phase(wiring_graph, A)

        if cost < current_best_cost:
            current_best_cut = cut
            current_best_cost = cost

    return tuple(current_best_cut)

def minimum_cut_phase(wiring_graph, merged_nodes):
    temp_graph = deepcopy(wiring_graph)
    temp_merged = deepcopy(merged_nodes)
    start = next(iter(wiring_graph))
    second_last_added = None
    last_added = start
    print("min phase", len(wiring_graph))

    while len(temp_graph) > 1:
        second_last_added = last_added
        last_added = most_tightly_connected(temp_graph, start)
        temp_graph, temp_merged = merge_nodes(temp_graph, temp_merged, (start, last_added))

    vertex_to_merge = (last_added, second_last_added)
    res_graph, res_merged = merge_nodes(wiring_graph, merged_nodes, vertex_to_merge)
    A = {start}.union(temp_merged[start]).difference({last_added})
    
    return res_graph, res_merged, A

def most_tightly_connected(wiring_graph, key):
    return max(wiring_graph[key].keys(), key=lambda x: wiring_graph[key][x])

def cut_of_the_phase(wiring_graph, A):
    cut = set()
    cost = 0

    for key in A:
        not_in_a = set(wiring_graph[key].keys()).difference(A)
        for other_key in not_in_a:
            cost += 1
            cut.add((key, other_key))
    
    return cut, len(cut)

def merge_nodes(wiring_graph, merged_nodes, vertex):
    node1, node2 = vertex
    copied_wiring_graph = deepcopy(wiring_graph)
    copied_merged_nodes = deepcopy(merged_nodes)

    copied_wiring_graph[node1].pop(node2, None)
    copied_wiring_graph[node2].pop(node1, None)
    node2_connections = copied_wiring_graph.pop(node2, dict())

    for key, value in node2_connections.items():
        copied_wiring_graph[node1][key] += value
        copied_wiring_graph[key].pop(node2, None)
        copied_wiring_graph[key][node1] = copied_wiring_graph[node1][key]

    node2_merged = copied_merged_nodes.pop(node2, set())

    copied_merged_nodes[node1].add(node2)
    copied_merged_nodes[node1].union(node2_merged)

    return copied_wiring_graph, copied_merged_nodes

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    wiring_diagram = {k: list(v.split()) for k, v in [x.split(":") for x in data.split("\n")]}

    print("Part 1:", prod(get_group_sizes(wiring_diagram, deterministic=False)))
    # print("Part 1:", prod(get_group_sizes(wiring_diagram, deterministic=True)))
    print("Part 2:", 0)