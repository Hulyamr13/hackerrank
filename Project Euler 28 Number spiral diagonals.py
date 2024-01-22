def sum_of_diagonals(N):
    if N == 1:
        return 1
    else:
        n = N // 2
        return (1 + 4 * (n * 6 + 9 * n * (n - 1) // 2 + 2 * (n - 1) * n * (2 * n - 1) // 3)) % 1000000007

def main():
    t = int(input().strip())
    for _ in range(t):
        N = int(input().strip())
        result = sum_of_diagonals(N)
        print(result)

if __name__ == "__main__":
    main()
