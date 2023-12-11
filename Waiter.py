def get_primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int(((n - i * i - 1) / (2 * i) + 1))
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def waiter(number, q):
    bp = number[:]  # badplate (not divisible)
    gp = []  # goodplate (divisible)
    tp = []  # tempplate (holder for plates that are not divisible)

    primes = get_primes(10000)  # Magic number to get a little over 1200 primes
    p = 0
    current_prime = primes[0]

    while p < q:
        while bp:
            cur = bp.pop()
            if cur % current_prime == 0:
                gp.append(cur)
            else:
                tp.append(cur)

        p += 1
        current_prime = primes[p]

        while gp:
            yield gp.pop()

        bp = tp[:]
        tp.clear()

    while bp:
        yield bp.pop()  # Yield remaining bad plates

# Example Usage:
n, q = map(int, input().split())
vals = list(map(int, input().split()))

result = waiter(vals, q)

for plate in result:
    print(plate)
