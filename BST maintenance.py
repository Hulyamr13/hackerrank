from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.size = 1
        self.h = 0
        self.left = None
        self.right = None
        self.parent = None

def add_edge(a, b, graph):
    graph[a].append(b)
    graph[b].append(a)

def build_graph(root, graph):
    if root is None:
        return
    if root.left is not None:
        add_edge(root.val, root.left.val, graph)
    if root.right is not None:
        add_edge(root.val, root.right.val, graph)
    build_graph(root.left, graph)
    build_graph(root.right, graph)

def find_all(v, graph, d=0, par=-1):
    ans = d
    for i in range(len(graph[v])):
        if graph[v][i] != par:
            ans += find_all(graph[v][i], graph, d + 1, v)
    return ans

def count_for_tree(n, root, graph):
    g = defaultdict(list)
    build_graph(root, g)
    ret = 0
    for i in range(n):
        ret += find_all(i, g)
    return ret // 2

def solve_stupid(n, p):
    root = Node(p[0])
    ret = [0]
    graph = defaultdict(list)
    for i in range(1, n):
        cur = root
        while True:
            if cur.val > p[i]:
                if cur.left is None:
                    cur.left = Node(p[i])
                    cur.left.parent = cur
                    break
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(p[i])
                    cur.right.parent = cur
                    break
                else:
                    cur = cur.right
        ret.append(count_for_tree(n, root, graph))
    return ret

