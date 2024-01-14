import functools, operator as op, sys

MAX = 10**18
MOD = 1000000007

FIBONACCI = [1, 2]
while FIBONACCI[-1] <= MAX:
    FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])

POWERS = [pow(2, i) for i in range(len(FIBONACCI))]

def zeckendorf_number(n):
    result = 0
    for i in reversed(range(len(FIBONACCI))):
        if n >= FIBONACCI[i]:
            result += POWERS[i]
            n -= FIBONACCI[i]
    return result

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    print(functools.reduce(op.xor, (zeckendorf_number(a) for a in A)) % MOD)
