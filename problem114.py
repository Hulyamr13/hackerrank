A = set(map(int, input().split())) # set A
n = int(input()) # number of other sets

is_superset = True

for i in range(n):
    B = set(map(int, input().split())) # set B
    if not B.issubset(A) or B == A:
        is_superset = False
        break

print(is_superset)