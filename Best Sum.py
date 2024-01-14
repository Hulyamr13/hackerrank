from math import atan2, pi

T = int(input())
for _ in range(T):
    N = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    f = [atan2(x, y) / pi for x, y in zip(a, b)]

    fab = list(zip(f, a, b))
    fab.sort()
    ab = [(a, b) for _, a, b in fab]
    ab = ab * 2

    max_ab = 0
    for low_ind in range(len(f)):
        sa = 0
        sb = 0
        for hi_ind in range(len(f)):
            sa += ab[low_ind + hi_ind][0]
            sb += ab[low_ind + hi_ind][1]
            if (sa ** 2 + sb ** 2) > max_ab:
                max_ab = sa ** 2 + sb ** 2
    print(max_ab)
