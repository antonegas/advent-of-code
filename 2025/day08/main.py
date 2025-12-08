def create_disjoint_sets(amount: int) -> tuple[list[int], list[int]]:
    parent = list()
    rank = list()

    for i in range(amount + 1):
        parent.append(i)
        rank.append(0)

    return parent, rank

def disjoint_set_union(x: int, y: int, parent: list[int], rank: list[int]):
    x_parent = disjoint_set_find(x, parent)
    y_parent = disjoint_set_find(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            y_parent, x_parent = x_parent, y_parent
        parent[y_parent] = x_parent
        if rank[x_parent] == rank[y_parent]:
            rank[x_parent] += 1

def disjoint_set_find(x: int, parent: list[int]) -> int:
    if x == parent[x]:
        return x
    
    parent[x] = disjoint_set_find(parent[x], parent)
    return parent[x]

def disjoint_set_same(x: int, y: int, parent: list[int]):
    return disjoint_set_find(x, parent) == disjoint_set_find(y, parent)

def kruskals(edges: list[tuple[float, int, int]], nodes: list[tuple[int, int, int]]) -> tuple[float, int]:    
    tree = list()
    vertices = len(nodes)

    parent, rank = create_disjoint_sets(vertices)
    sorted_edges = (sorted(edges))

    count = 0
    part1 = 0
    part2 = 0

    for w, u, v in sorted_edges:
        if not disjoint_set_same(u, v, parent):
            tree.append((w, u, v))
            disjoint_set_union(u, v, parent, rank)
            part2 = nodes[u][0] * nodes[v][0]
        count += 1

        if count == 1000:
            circuit_size = [0] * vertices
            for i in range(vertices):
                circuit_size[disjoint_set_find(i, parent)] += 1

            largest = list(reversed(sorted(circuit_size)))
            part1 = largest[0] * largest[1] * largest[2]

    return part1, part2

def create_edges(nodes: list[tuple[int, int, int]]) -> list[tuple[float, int, int]]:
    edges = list()

    for u in range(len(nodes)):
        x1, y1, z1 = nodes[u]

        for v in range(u + 1, len(nodes)):
            x2, y2, z2 = nodes[v]

            edges.append((((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5, u, v))

    return edges

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    l = data.split("\n")
    nodes = [tuple(map(int, x.split(","))) for x in l]
    edges = create_edges(nodes)

    part1, part2 = kruskals(edges, nodes)

    print("Part 1:", part1)
    print("Part 2:", part2)