def main():
    tests = int(input())
    for _ in range(tests):
        n, k = map(int, input().split())
        d = [0] * (k + 1)
        for i in range(k):
            d[i] = n // k
            if n % k >= i and i > 0:
                d[i] += 1

        ans = 0
        for i in range(k):
            p = k - i
            if p == k:
                p = 0
            if p > i:
                ans += d[i] * d[p]
            elif p == i:
                ans += d[i] * (d[p] - 1) // 2

        print(ans)


if __name__ == "__main__":
    main()
