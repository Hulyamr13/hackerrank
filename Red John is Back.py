def primes(n):
    """ Returns  a list of primes < n """
    if n <= 2: return 0
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return len([i for i in range(3, n, 2) if sieve[i]]) + 1


def find_configs(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0

    return find_configs(N - 1) + find_configs(N - 4)


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        result = primes(find_configs(N) + 1)
        print(result)


if __name__ == "__main__":
    main()
