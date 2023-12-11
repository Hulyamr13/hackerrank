import os


def powerrr(a, b, M):
    fin = 1
    while b:
        if b & 1:
            fin = (fin * a) % M
        a = (a * a) % M
        b >>= 1
    return fin


def inv(x, M):
    return powerrr(x, M - 2, M)


def calculatiosn(n, M):
    ans1 = [0] * (n + 1)
    ans2 = [0] * (n + 1)
    ans1[0] = ans2[0] = 1
    for i in range(1, n + 1):
        ans1[i] = (ans1[i - 1] * i) % M
        ans2[i] = (ans2[i - 1] * inv(i, M)) % M
    return ans1, ans2


def uniqueDivideAndConquer(n, m):
    ans1, ans2 = calculatiosn(n, m)
    f = [0] * (n + 1)
    dp = [0] * (n + 1)
    f[1] = 1
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        f[i] = dp[i - 1]
        for j in range((i + 1) // 2, i):
            cur1 = (f[j] * ans1[i - 1]) % m  # cnk(i - 1, j)
            cur2 = (cur1 * ans2[j]) % m
            cur3 = (cur2 * ans2[i - 1 - j]) % m
            cur4 = (cur3 * j) % m
            f[i] -= (cur4 * dp[i - j - 1]) % m
            if f[i] < 0:
                f[i] += m
        f[i] = (f[i] * i) % m
        for j in range(1, i + 1):
            cur1 = (f[j] * ans1[i - 1]) % m
            cur2 = (cur1 * ans2[j - 1]) % m
            cur3 = (cur2 * ans2[i - j]) % m
            cur4 = (cur3 * j) % m
            dp[i] = (dp[i] + cur4 * dp[i - j]) % m
    return f[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = uniqueDivideAndConquer(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
