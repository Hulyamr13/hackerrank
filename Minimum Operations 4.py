def min_operations(red, green, blue):
    n = len(red)
    dp = [[1 << 30] * (1 << 3) for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(n):
        for j in range(1 << 3):
            dp[i + 1][j | 1] = min(dp[i + 1][j | 1], dp[i][j] + green[i] + blue[i])
            dp[i + 1][j | 2] = min(dp[i + 1][j | 2], dp[i][j] + red[i] + blue[i])
            dp[i + 1][j | 4] = min(dp[i + 1][j | 4], dp[i][j] + red[i] + green[i])

    j = 0
    for i in range(n):
        if red[i]:
            j |= 1
        if green[i]:
            j |= 2
        if blue[i]:
            j |= 4

    if dp[n][j] >= (1 << 30):
        dp[n][j] = -1

    return dp[n][j]

if __name__ == "__main__":
    n = int(input())
    red, green, blue = [], [], []
    for i in range(n):
        r, g, b = map(int, input().split())
        red.append(r)
        green.append(g)
        blue.append(b)

    print(min_operations(red, green, blue))
