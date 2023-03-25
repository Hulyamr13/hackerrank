from collections import deque

L = ['No', 'Yes']
T = int(input())
for i in range(T):
    t = True
    N = int(input())
    b = deque(map(int, input().split()), maxlen=N)
    m = max(b[0], b[-1])
    while b:
        if b[0] >= b[-1]:
            c = b.popleft()
        else:
            c = b.pop()
        if m >= c:
            m = c
        else:
            t = False
            break
    print(L[t])
