# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 1000000007

def main():
    increase = 0
    decrease = 0

    inc = [[0] * 20 for _ in range(100010)]
    dec = [[0] * 20 for _ in range(100010)]
    ans = [0] * 100010
    n = 100000

    for i in range(1, n):
        for j in range(10):
            for k in range(10):
                if k >= j:
                    if i == n - 1 or j > 0:
                        inc[i][j] = (inc[i][j] + inc[i - 1][k] + (10 - k)) % MOD
                if k <= j:
                    dec[i][j] = (dec[i][j] + dec[i - 1][k] + (k + 1)) % MOD

        increase = inc[i][1] + 9
        decrease = dec[i][9] - (10 * dec[i][0])
        ans[i + 1] = (increase + decrease) % MOD

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(ans[n])

if __name__ == "__main__":
    main()
