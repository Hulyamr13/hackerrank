import heapq

def solve_zombie_population(num_test_cases):
    while num_test_cases > 0:
        N, M, k = map(int, input().split())

        edges = {}

        for _ in range(M):
            start, end = map(int, input().split())
            if start not in edges:
                edges[start] = [0.0, []]
            if end not in edges:
                edges[end] = [0.0, []]
            edges[start][0] += 1.0
            edges[start][1].append(end)
            edges[end][0] += 1.0
            edges[end][1].append(start)

        nodes = []

        for _ in range(N):
            nodes.append(int(input()))

        output = calculate_zombie_population(nodes, edges, k)
        print(" ".join(map(str, output)))
        num_test_cases -= 1

def calculate_zombie_population(nodes, edges, k):
    length = len(nodes)
    first_buf = nodes
    second_buf = [0] * length
    while k > 0:
        for i in range(length):
            neighbors = edges[i][1]
            neighbor_len = edges[i][0]
            num = first_buf[i] / neighbor_len
            for j in neighbors:
                second_buf[j] += num

        first_buf, second_buf = second_buf, first_buf
        for i in range(length):
            if abs(first_buf[i] - second_buf[i]) > 0.0001:
                break
            if i == length - 1:
                return [str(int(round(x))) for x in heapq.nlargest(5, first_buf)]
        for i in range(length):
            second_buf[i] = 0
        k -= 1
    return [str(int(round(x))) for x in heapq.nlargest(5, first_buf)]

if __name__ == "__main__":
    num_test_cases = int(input())
    solve_zombie_population(num_test_cases)
