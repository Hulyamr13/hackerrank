from collections import defaultdict

MOD = 1_000_000_009


class Node:
    def __init__(self):
        self.nf = set()
        self.out_edges = dict()

    def add(self, v):
        self.nf.add(v)
        self.out_edges[v] = dict()
        return self

    def __len__(self):
        return len(self.out_edges)


class Graph2:
    def __init__(self):
        self.vertices = defaultdict(Node)
        self.weights = dict()

    def add_edge(self, u, v, w):
        self.weights[(min(u, v), max(u, v))] = w
        self.vertices[u].add(v)
        self.vertices[v].add(u)
        return self

    def leaves(self):
        return set(u for u, node in self.vertices.items() if len(node) == 1)

    def node(self, u):
        return self.vertices[u]

    def weight(self, u, v):
        u, v = (u, v) if u < v else (v, u)
        return self.weights[(u, v)]

    def __len__(self):
        return len(self.vertices)

    def calculate_frequencies(self):
        updateables = self.leaves()
        while updateables:
            v = updateables.pop()
            updateables.update(update_frequencies(v, self))


def frequency_sum(node, v, w=0):
    freq = dict()
    freq[2] = (w, 1)
    for u, e in node.out_edges.items():
        if u == v:
            continue
        for k, (f, n) in e.items():
            f0, n0 = freq.get(k + 1, (0, 0))
            freq[k + 1] = ((f0 + f + n * w) % MOD, n0 + n)
    return freq


def update_frequencies(u, G):
    node = G.node(u)
    assert (len(node.nf) <= 1)
    nodes = node.nf if len(node.nf) == 1 else node.out_edges.keys()
    updateable = set()
    for v in nodes:
        other = G.node(v)
        if not other.nf:
            continue
        if u in other.nf:
            other.nf.discard(u)
            other.out_edges[u] = frequency_sum(node, v, G.weight(u, v))
        if len(other.nf) <= 1:
            updateable.add(v)
    return updateable


class ModularFactorial:
    def __init__(self):
        self.value = 1

    def __call__(self, i):
        current_value = self.value
        self.value = (self.value * i) % MOD
        return current_value


def factorial_per_k(n):
    factorial = ModularFactorial()
    x = [factorial(i) for i in range(1, n + 1)]
    factorial = ModularFactorial()
    y = [factorial(i) for i in range(n, 0, -1)]

    return [(xi * yi) % MOD for xi, yi in zip(x, reversed(y))]


def calculate_magic(G):
    G.calculate_frequencies()
    magic = 0
    factorials_per_k = factorial_per_k(len(G))
    for node in G.vertices.values():
        magic = sum((((v * factorials_per_k[k - 1]) % MOD)
                     for out in node.out_edges.values()
                     for k, (v, n) in out.items()),
                    start=(magic % MOD))
    return magic % MOD


if __name__ == '__main__':
    n = int(input())
    graph = Graph2()
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)
    print(calculate_magic(graph))
