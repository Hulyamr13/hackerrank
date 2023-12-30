MAX_N = 5000
MOD = int(1E9 + 9)

def main():
    ways = [1] * (MAX_N + 1)

    for i in range(1, MAX_N + 1):
        for j in range(i):
            ways[i] += ways[j] * ways[i-1-j]
            ways[i] %= MOD

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ways[n] - 1)

if __name__ == "__main__":
    main()
