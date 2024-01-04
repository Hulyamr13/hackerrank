# Enter your code here. Read input from STDIN. Print output to STDOUT

from functools import wraps


def memoize(function):
    memo = {}

    @wraps(function)
    def f(*args, **kwargs):
        key = args, tuple(sorted(kwargs.items()))
        if key not in memo:
            memo[key] = function(*args, **kwargs)
        return memo[key]

    f.memo = memo
    return f


def g(w, p):
    lft = max(0, w - p + 1)
    ryt = min(p, w + 1)
    return max(0, ryt - lft)


@memoize
def f(k, n, c, p):
    if n == 0:
        if k == 0:
            return c == 0
        return 0
    if k < 0:
        return 0
    return f(k, n // p, 0, p) * g(n % p - c, p) + f(k - 1, n // p, 1, p) * g(n % p + p - c, p)


if __name__ == "__main__":
    for cas in range(int(input())):
        n, p = map(int, input().strip().split())
        lc = 3
        nm = n
        while nm:
            nm //= p
            lc += 1

        f.memo.clear()
        v = [f(l, n, 0, p) for l in range(lc)]

        while lc >= 0 and v[lc - 1] == 0:
            lc -= 1

        print(' '.join(str(v[i]) for i in range(lc)))
