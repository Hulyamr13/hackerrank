# Enter your code here. Read input from STDIN. Print output to STDOUT

MAX = 10 ** 12


def F(n, b):
    e = (b - n ** 2)
    power1 = int(2 ** e)
    power2 = 10 ** 9

    return power1 / power2


u, b = map(float, input().split())

prev = u
found = set([u])

for i in range(1, MAX + 1):
    next = F(prev, b)

    if next in found and prev in found:
        break

    found.add(next)
    prev = next

print('{:.9f}'.format(next + prev))
