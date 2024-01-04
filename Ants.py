N = int(input())
V = list(map(int, input().split()))
V.sort()

x = N // 2
H = (N - x) * x * 400000

in_a_row = 1
last = V[0]

for v in V[1:]:
    if v - 1 == last:
        in_a_row += 1
    else:
        H += in_a_row - in_a_row % 2
        in_a_row = 1
    last = v

H += in_a_row - in_a_row % 2

print(H)
