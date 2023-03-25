if __name__ == "__main__":
    n = int(input().strip())
    total_edge_multiplier = 0
    total_vertex_multiplier = 0
    graph = {i: [] for i in range(1, n + 1)}
    for a0 in range(n - 1):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        graph[x].append(y)
        graph[y].append(x)
    frontier = {1: 0}
    explored = {}
    root_distance = 0
    while frontier != {}:
        total_vertex_multiplier += root_distance * (root_distance + 1) / 2 * len(frontier)
        new_frontier = {}
        root_distance += 1
        for v in frontier:
            explored[v] = 0
        for v1 in frontier:
            for v2 in graph[v1]:
                if v2 not in explored:
                    new_frontier[v2] = 0
                    total_edge_multiplier += root_distance
        frontier = new_frontier

    print("{:.10f}".format(n - total_vertex_multiplier / total_edge_multiplier))