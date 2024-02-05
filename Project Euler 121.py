# Enter your code here. Read input from STDIN. Print output to STDOUT

prev = {(0, 0): 1}
M = {}

for move in range(65):
    M[move] = [0, 0]
    _next = {}

    for poss, count in sorted(prev.items()):
        if poss[0] > poss[1]:
            M[move][0] += count
        M[move][1] += count

        a = (poss[0], poss[1] + 1)
        b = (poss[0] + 1, poss[1])

        _next[a] = _next.get(a, 0) + count * (move + 1)
        _next[b] = _next.get(b, 0) + count

    prev = _next

T = int(input())

for _ in range(T):
    N = int(input())
    print(M[N][1] // M[N][0])
