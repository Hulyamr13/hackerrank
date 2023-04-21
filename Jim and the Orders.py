def solve():
    n = int(input())
    a = [(tuple(map(int, input().split()))) for _ in range(n)]
    a = [(i + 1, a[i][0], a[i][1]) for i in range(n)]
    a = [(x[0], x[1] + x[2]) for x in a]
    a = sorted(a, key=lambda x: x[1])
    a = [x[0] for x in a]
    print(" ".join(list(map(str, a))))


if __name__ == "__main__":
    solve()