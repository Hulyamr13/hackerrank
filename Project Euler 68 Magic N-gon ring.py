# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import permutations

ans = set()
N, S = map(int, input().split())
limit = N * 2 + 1

def solve(ring, used, i):
    global ans
    if i == N - 1:
        a = (S - ring[i][1]) - ring[i][2]
        if a < 1 or a >= limit or used[a]:
            return
        ring[i][0] = a
        res = ""
        for j in range(N):
            if ring[j][0] < ring[0][0]:
                return
            res += ''.join(map(str, ring[j]))
        ans.add(res)
        return

    for j in range((ring[0][0] + 1) if i > 0 else 1, limit):
        a = (S - ring[i][1]) - j
        if a < 1:
            break
        if a >= limit or a == j:
            continue
        if used[j] or used[a]:
            continue

        next_ring = [row[:] for row in ring]
        used_temp = used.copy()

        used_temp[j] = True
        used_temp[a] = True
        next_ring[i][0] = j
        next_ring[i][2] = a

        if i < N - 1:
            next_ring[i + 1][1] = a

        solve(next_ring, used_temp, i + 1)

for i in range(1, limit):
    ring = [[-1, i, -1] for _ in range(N)]
    used = [False] * limit

    ring[0][1] = i
    ring[N - 1][2] = i
    used[i] = True

    solve(ring, used, 0)

result = '\n'.join(sorted(ans))
print(result)
