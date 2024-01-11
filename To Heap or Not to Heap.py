# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

mod = 10 ** 9 + 7

catalan_cache = {}


def catalan(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if n in catalan_cache:
        return catalan_cache[n]
    top = 1
    for i in range(n + 1, n + n + 1):
        top = (top * i) % mod
    bottom = 1
    for i in range(1, n + 2):
        bottom = (bottom * i) % mod
    result = (top * pow(bottom, mod - 2, mod)) % mod
    catalan_cache[n] = result
    return result


n = int(input())
a = list(map(int, input().split()))

bigger = [len(a)] * len(a)
back = [i - 1 for i in range(len(a))]
for i in range(1, len(a)):
    ci = i - 1
    while ci >= 0 and a[ci] < a[i]:
        bigger[ci] = i
        ci = back[ci]
        back[i] = ci

grow_count = [0, 0]
c = 0
for i in range(1, n):
    if a[i - 1] < a[i]:
        c += 1
    grow_count.append(c)

cache = collections.defaultdict(dict)


def count(a, start, finish):
    l = finish - start
    if l == 1:
        return 1

    if grow_count[finish] - grow_count[start] == 0:
        return catalan(l // 2)

    if finish in cache[start]:
        return cache[start][finish]
    result = 0
    i = start + 2
    if bigger[start + 1] < finish:
        i = bigger[start + 1]
        if (i - start) & 1:
            return 0

    while i < finish:
        if bigger[start + 1] < i:
            break
        if bigger[i] >= finish:
            if i - start - 1 < finish - i:
                left = count(a, start + 1, i)
                if left:
                    result += left * count(a, i, finish) % mod
            else:
                right = count(a, i, finish)
                if right:
                    result += count(a, start + 1, i) * right % mod
        i += 2
    result %= mod
    cache[start][finish] = result
    return result


if bigger[0] < len(a):
    print(0)
else:
    print(count(a, 0, len(a)))
