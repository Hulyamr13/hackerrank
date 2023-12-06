MOD = 10 ** 9 + 9
N = 10 ** 5
K = 26

class Solver(object):
    def __init__(self):
        self.factorials = [1 for _ in range(26 + 1)]
        for i in range(1, 26 + 1):
            self.factorials[i] = self.factorials[i - 1] * i

        self.F = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        for j in range(1, K + 1):
            self.F[1][j] = j
            for i in range(2, N + 1):
                if i % 2 == 0:
                    self.F[i][j] = self.F[i - 1][j] * j - self.F[i // 2][j]
                else:
                    self.F[i][j] = self.F[i - 1][j] * j
                self.F[i][j] %= MOD

        self.G = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

        for j in range(1, K + 1):
            total = j
            for i in range(1, N + 1):
                self.G[i][j] = total - self.F[i][j]
                self.G[i][j] %= MOD
                total *= j
                total %= MOD

    def solve(self, n, k):
        P = 0
        if k == 1:
            P += self.G[n][k]
        else:
            for j in range(k, 0, -1):
                P += (-1) ** (k - j) * self.G[n][j] * (
                    self.factorials[k] // (self.factorials[j] * self.factorials[k - j]))
                P %= MOD

        res = P * (self.factorials[26] // (self.factorials[k] * self.factorials[26 - k]))
        return res % MOD


if __name__ == "__main__":
    import sys

    testcases = int(input())
    solver = Solver()
    for _ in range(testcases):
        n, k = map(int, input().split())
        print(solver.solve(n, k))