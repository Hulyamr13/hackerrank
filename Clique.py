def solve1(n, k):
    g1 = n % k
    g2 = k - g1
    sz1 = n // k + 1
    sz2 = n // k
    ret = g1 * sz1 * g2 * sz2 + g1 * (g1 - 1) * sz1 * sz1 // 2 + g2 * (g2 - 1) * sz2 * sz2 // 2
    return ret

def solve(n, e):
    low = 1
    high = n + 1
    while low + 1 < high:
        mid = low + (high - low) // 2
        k = solve1(n, mid)
        if k < e:
            low = mid
        else:
            high = mid
    return high

if __name__ == '__main__':
    runs = int(input())
    for _ in range(runs):
        n, k = map(int, input().split())
        ret = solve(n, k)
        print(ret)