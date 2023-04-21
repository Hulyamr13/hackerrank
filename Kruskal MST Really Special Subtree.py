import os

# Define a class to represent a disjoint set
class DisjointSet:
    def __init__(self, nodes):
        self.parent = [i for i in range(nodes)]
        self.rank = [0 for _ in range(nodes)]

    # Find the root of the set
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union two sets
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

# Define a function to implement Kruskal's algorithm
def kruskals(g_nodes, g_from, g_to, g_weight):
    # Create a disjoint set for all nodes
    disjoint_set = DisjointSet(g_nodes)

    # Sort the edges by weight in ascending order
    edges = list(zip(g_from, g_to, g_weight))
    edges.sort(key=lambda x: x[2])

    # Initialize total weight of the subtree to 0
    total_weight = 0

    # Iterate through all edges and add them to the subtree if they don't create a cycle
    for edge in edges:
        x = disjoint_set.find(edge[0] - 1)
        y = disjoint_set.find(edge[1] - 1)
        if x != y:
            disjoint_set.union(x, y)
            total_weight += edge[2]

    return total_weight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')

    fptr.close()
