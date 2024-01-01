MOD = 10 ** 9

def init():
    f = [[0] * 1001 for _ in range(1001)]
    for i in range(1, 1001):
        f[i][0] = f[i][i] = 1
        for j in range(1, i):
            f[i][j] = (f[i - 1][j - 1] + f[i - 1][j]) % MOD
    return f


def solve(t, inputs):
    f = init()
    results = []
    for i in range(t):
        n, k = inputs[i]
        result = f[n + k - 1][n - 1]
        results.append(result)
    return results


if __name__ == "__main__":
    t = int(input().strip())
    inputs = []
    for _ in range(t):
        n = int(input().strip())
        k = int(input().strip())
        inputs.append((n, k))
    results = solve(t, inputs)
    for res in results:
        print(str(res)[-9:])
