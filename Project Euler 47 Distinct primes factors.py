# Enter your code here. Read input from STDIN. Print output to STDOUT

def sieve(N):
    is_prime = [0] * (N + 1)
    for i in range(2, N + 1):
        if not is_prime[i]:
            for j in range(i, N + 1, i):
                is_prime[j] += 1
    return is_prime

def main():
    N = 2000 * 1000
    is_prime = sieve(N)
    n, k = map(int, input().split())
    for i in range(2, n + 1):
        flag = False
        for j in range(k):
            if is_prime[i + j] != k:
                flag = True
                break
        if not flag:
            print(i)

if __name__ == "__main__":
    main()
