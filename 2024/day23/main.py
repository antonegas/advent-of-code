from collections import defaultdict, deque
import networkx as nx

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    connections = {tuple(x.split("-")) for x in data.split("\n")}

    part2 = ""

    devices = set()

    for connection in connections:
        c1, c2 = connection
        devices.add(c1)
        devices.add(c2)

    G = nx.Graph()
    G.add_nodes_from(devices)
    G.add_edges_from(connections)

    cliques = nx.enumerate_all_cliques(G)
    
    groups = list()

    for clique in cliques:
        if len(clique) > 3:
            break
        if len(clique) == 3:
            groups.append(clique)

    max_clique = list(list(cliques)[-1])

    for c in sorted(max_clique):
        part2 += f"{c},"

    print("Part 1:", len([x for x in groups if any([y[0] == "t" for y in x])]))
    print("Part 2:", part2[:-1])