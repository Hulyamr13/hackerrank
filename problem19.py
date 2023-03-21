import itertools


def f(x):
    return x**2


k, m = map(int, input().split())

lists = []
for i in range(k):
    ni, *elements = map(int, input().split())
    lists.append(elements)

max_sum = 0
for xs in itertools.product(*lists):
    s = sum(f(x) for x in xs) % m
    if s > max_sum:
        max_sum = s

print(max_sum)
