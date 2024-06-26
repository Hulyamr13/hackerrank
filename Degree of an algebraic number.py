from itertools import product
import sys

def print_matrix(matrix):
    print('\n'.join(''.join(map(str, row)) for row in matrix))

def eratosthenes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    falses = [False] * (n // 2)
    curr = 2
    while curr * curr <= n:
        sieve[curr * 2:: curr] = falses[:(n // curr) - 1]
        curr += 1
        while not sieve[curr]:
            curr += 1
    return [x for x in range(n) if sieve[x]]

primes = eratosthenes_sieve(4000)

def factorize_number(n):
    factors = list()
    for p in primes:
        if p * p > n:
            break
        power = 0
        while n % p == 0:
            power += 1
            n //= p
        if power % 2 == 1:
            factors.append(p)
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors

def gauss_jordan_elimination(matrix, debug=False):
    n, m = len(matrix), len(matrix[0])
    pivot_row, pivot_col = 0, 0
    while pivot_row < n and pivot_col < m:
        i_max = None
        for i in range(pivot_row, n):
            if matrix[i][pivot_col] == 1:
                i_max = i
                break
        if i_max is None:
            pivot_col += 1
            continue
        else:
            if pivot_row != i_max:
                if debug:
                    print("Swapping row %d and %d" % (pivot_row, i_max))
                matrix[pivot_row], matrix[i_max] = matrix[i_max], matrix[pivot_row]
                if debug:
                    print_matrix(matrix)
            for i in range(pivot_row + 1, n):
                if matrix[i][pivot_col] == 1:
                    if debug:
                        print("Adding row %d to row %d" % (pivot_row, i))
                    for j in range(pivot_row, m):
                        matrix[i][j] ^= matrix[pivot_row][j]
                    if debug:
                        print_matrix(matrix)
            pivot_row += 1
            pivot_col += 1

def solve_matrix(A):
    A = [number for number in map(factorize_number, A) if number]
    if not A:
        return 0
    all_factors = set(x for number in A for x in number)
    prime_dict = {prime: rank for rank, prime in enumerate(all_factors)}
    matrix = [[0] * len(A) for _ in range(len(prime_dict))]
    for i, number in enumerate(A):
        for prime in number:
            matrix[prime_dict[prime]][i] = 1
    gauss_jordan_elimination(matrix)
    return sum(any(x > 0 for x in row) for row in matrix)

def all_matrices(n, m):
    for lists in product([0, 1], repeat=n * m):
        yield [list(lists[i * m: (i + 1) * m]) for i in range(n)]

T = int(sys.stdin.readline())
for caseno in range(T):
    N = int(sys.stdin.readline())
    A = map(int, sys.stdin.readline().split())
    print(2 ** solve_matrix(A))
