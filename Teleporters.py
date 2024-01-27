# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
adj = [set() for _ in range(n)]
telp = list(map(int, input().split()))

for _ in range(n - 1):
    a, b = (int(s) - 1 for s in input().split())
    adj[a].add(b)
    adj[b].add(a)

telp_q = [[] for _ in range(n)]
query = [[] for _ in range(m)]

num_cycle = min(120, m // 100 + 1)
changed_in = [[False] * num_cycle for _ in range(n)]

for i in range(num_cycle):
    changed_in[0][i] = True

for i in range(m):
    qu1 = list(map(int, input().split()))
    qu1[1] -= 1
    query[i] = qu1
    if qu1[0] == 1:
        telp_q[qu1[1]].append(i)
        if qu1[1] == 0:
            query[i][2] = 0
        changed_in[qu1[1]][(i * num_cycle) // m] = True

telp_q[0] = [0]

depth = [-1] * n
depth[0] = 0
real_parent_node = [-1] * n
real_parent_node[0] = 0
parent_node = [-1] * n
parent_node[0] = 0
parent_jmp = [0] * n
wait_stack = [0]
in_path = [0]
hopes = [0] * n

while wait_stack:
    parent_nd = wait_stack.pop()
    next_depth = depth[parent_nd] + 1
    if len(in_path) < next_depth:
        in_path.append(parent_nd)
    else:
        in_path[next_depth - 1] = parent_nd

    for i in adj[parent_nd]:
        if depth[i] == -1:
            depth[i] = next_depth
            wait_stack.append(i)
            telp_parent = in_path[max(0, next_depth - telp[i])]
            real_parent_node[i] = telp_parent

            for q in telp_q[i]:
                qu1 = query[q]
                query_depth = query[q][2]
                telp_parent = in_path[max(0, next_depth - query_depth)]
                query[q][2] = telp_parent  # Change query such meaning

arranged = sorted(range(n), key=lambda i: depth[i])

iter = 0
cycle = -1
for q in query:
    if iter * num_cycle // m > cycle:
        cycle = iter * num_cycle // m
        for node in arranged:
            rl_p = real_parent_node[node]
            if changed_in[rl_p][cycle]:
                parent_node[node] = rl_p
                parent_jmp[node] = 1
            else:
                parent_node[node] = parent_node[rl_p]
                parent_jmp[node] = parent_jmp[rl_p] + 1

    if q[0] == 1:
        rl_p = q[2]
        real_parent_node[q[1]] = rl_p
        if changed_in[rl_p][cycle]:
            parent_node[q[1]] = rl_p
            parent_jmp[q[1]] = 1
        else:
            parent_node[q[1]] = parent_node[rl_p]
            parent_jmp[q[1]] = parent_jmp[rl_p] + 1
    elif q[0] == 2:
        q_start = q[1]
        jump = 0
        while q_start > 0:
            jump += parent_jmp[q_start]
            q_start = parent_node[q_start]
        print(jump)

    iter += 1
