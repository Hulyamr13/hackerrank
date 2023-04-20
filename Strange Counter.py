t = int(input())
S = 1
init = 3
ans = None

while True:
    if S == t:
        ans = S+2
        break
    elif S + init > t:
        ans = S+2-(t-S)
        break
    S = S + init
    init = init * 2

print(ans)