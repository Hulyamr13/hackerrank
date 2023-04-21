from collections import defaultdict
from itertools import count


def tree_cut(n, costs, edges):
    edge_map = defaultdict(set)
    for x, y in edges:
        edge_map[x].add(y)
        edge_map[y].add(x)

    # Hierarchical sort
    visited = set()
    ordering = []
    children = defaultdict(list)
    stack = [1]
    while stack:
        node = stack.pop()
        visited.add(node)
        ordering.append(node)

        children[node] = clist = [
            c for c in edge_map[node]
            if c not in visited]
        stack.extend(clist)

    subtree_costs = {}
    for node in reversed(ordering):
        subtree_costs[node] = costs[node] + sum(
            subtree_costs[c] for c in children[node])
    total_cost = sum(costs.values())
    return min(abs(total_cost - 2 * subc)
               for subc in subtree_costs.values())


def main():
    n = int(input())
    costs = dict(zip(count(1), map(int, input().split())))
    edges = []
    for i in range(n - 1):
        x, y = input().split()
        edges.append((int(x), int(y)))
    print(tree_cut(n, costs, edges))


if __name__ == '__main__':
    main()
