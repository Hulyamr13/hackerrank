def compute_x():
    MOD = 10 ** 9 + 7
    L = 5000011
    x = [1] * L

    for i in range(2, L):
        x[i] = (MOD - MOD // i) * x[MOD % i] % MOD

    for i in range(1, L):
        x[i] = 2 * x[i] * x[i] % MOD

    return x


def calculate_infected(x, a, b):
    MOD = 10 ** 9 + 7
    a += 1
    b += 1
    a %= MOD
    b %= MOD
    m = min(a, b)
    t = p = 1

    for i in range(1, m):
        p *= (a - i) * (b - i) % MOD * x[i]
        p %= MOD
        if p == 0:
            break
        t += p

    return t % MOD


def main():
    x_values = compute_x()
    test_cases = int(input())

    for _ in range(test_cases):
        a, b = map(int, input().strip().split())
        result = calculate_infected(x_values, a, b)
        print(result)


if __name__ == "__main__":
    main()
