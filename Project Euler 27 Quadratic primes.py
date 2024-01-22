# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

def is_prime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def find_solutions(n):
    max_consec = 0
    solutions = []
    for i in itertools.product(list(range(-n, n + 1, 1)), range(n + 1)):
        primes = 0
        x = 0
        while True:
            abc = x**2 + i[0]*x + i[1]
            if abc < 0:
                break
            if not is_prime(abc):
                break
            x += 1
            primes += 1
        if primes > max_consec:
            solutions.append(i)
            max_consec = primes
    return solutions

n = int(input())
result = find_solutions(n)
print(*result[-1])

