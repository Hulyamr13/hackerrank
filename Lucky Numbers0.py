import math

primes = [False] * 2000
mem = [[[None] * 19 for _ in range(2000)] for _ in range(200)]

def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def dp(sum, sum_sq, z):
    if mem[sum][sum_sq][z] is not None:
        return mem[sum][sum_sq][z]

    count = 0
    if z == 0:
        count = 1 if primes[sum] and primes[sum_sq] else 0
    else:
        for i in range(10):
            count += dp(sum + i, sum_sq + i * i, z - 1)

    mem[sum][sum_sq][z] = count
    return count

def lucky_upto(A):
    b = 0
    f = 10 ** 18
    sum = 0
    sum_sq = 0
    z = 18

    while f > A:
        f //= 10
        z -= 1

    count = 0

    for i in range(z, -1, -1):
        for j in range(10):
            max_val = b + f * (j + 1) - 1
            if A == max_val:
                count += dp(sum + j, sum_sq + j * j, i)
                return count
            elif A > max_val:
                count += dp(sum + j, sum_sq + j * j, i)
            else:
                sum += j
                sum_sq += j * j
                b += j * f
                f //= 10
                break

    return count

def main():
    for i in range(2, len(primes)):
        primes[i] = isprime(i)

    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        if A == 10 ** 18:
            A -= 1
        if B == 10 ** 18:
            B -= 1

        print(lucky_upto(B) - lucky_upto(A - 1))

if __name__ == '__main__':
    main()