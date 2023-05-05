from collections import deque

def compute_parity(n, G):
    parity = [True for i in range(n)]
    order = [[-1,-1] for i in range(n)]
    total = 0
    pre = 0
    post = 0
    parent = deque([0])
    while (len(parent) > 0):
        node = parent.pop()
        if (order[node][0] == -1):
            order[node][0] = pre
            pre += 1
            parity[node] = not parity[G[node][1]]
            if (parity[node]):
                total = total ^ G[node][0]
            G[node][2].remove(G[node][1])
            if (len(G[node][2]) == 0):
                parent.append(node)
            else:
                for c in G[node][2]:
                    G[c][1] = node
                    parent.append(c)
        else:
            order[node][1] = post
            post += 1
            for c in G[node][2]:
                G[node][0] = G[node][0] ^ G[c][0]
            if (G[G[node][1]][2][0] == node):
                parent.append(G[node][1])
    return parity, order, total

def answer_queries(q, parity, order, G, total):
    for i in range(q):
        u, v = (int(vertex)-1 for vertex in input().strip().split())
        if (order[u][0] < order[v][0] and order[u][1] > order[v][1]):
            print("INVALID")
        elif (parity[u] == parity[v]):
            newtotal = G[u][0]
            if (newtotal ^ total == 0):
                print("NO")
            else:
                print("YES")
        else:
            if (total == 0):
                print("NO")
            else:
                print("YES")

def main():
    n = int(input())
    G = [[int(c), 0, []] for c in input().strip().split()]
    G[0][2].append(0)
    for i in range(n-1):
        v1, v2 = (int(v)-1 for v in input().strip().split())
        G[v1][2].append(v2)
        G[v2][2].append(v1)
    parity, order, total = compute_parity(n, G)
    q = int(input())
    answer_queries(q, parity, order, G, total)

if __name__ == '__main__':
    main()
