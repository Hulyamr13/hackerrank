PRIME = 1000003

def extended_gcd(a, b):
    """Return (r, s, d) where a*r + b*s = d and d = gcd(a,b)"""
    x, y = 0, 1
    lastx, lasty = 1, 0
    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return (lastx, lasty, a)

def modular_div(a, b, n):
    """Return a/d (mod n) assuming gcd(b,n) = 1"""
    return a * extended_gcd(b, n)[0] % n

def create_facs(prime):
    facs = [1]
    fac = 1
    for n in range(1, prime):
        fac = fac * n % prime
        facs.append(fac)
    return facs

FACS = create_facs(PRIME)

def comb(n, k):
    num = FACS[n]
    den = FACS[n - k] * FACS[k] % PRIME
    return modular_div(num, den, PRIME)

def lucas_theorem(n, k, prime):
    if n < prime:
        return 0 if n < k else comb(n, k)
    n, nm = divmod(n, prime)
    k, km = divmod(k, prime)
    if km > nm:
        return 0
    return lucas_theorem(n, k, prime) * comb(nm, km) % prime

def solution(n, k, prime):
    """from OEIS"""
    if k > n - 3:
        return 0
    x = (lucas_theorem(n - 1 + k, k, prime) * lucas_theorem(n - 3, k, prime)) % prime
    if k == prime - 1:
        sss = (n // prime - 1)
    else:
        sss = 0
    return modular_div(x, (k + 1), prime) + sss

def solution1(n, k, prime):
    """from OEIS"""
    if k > n - 3:
        return 0
    x = (lucas_theorem(n - 1 + k, k, prime) * lucas_theorem(n - 2, k + 1, prime)) % prime
    if k == prime - 1:
        sss = (n // prime - 1)
    else:
        sss = 0
    return x * (n - 3) % prime + sss

def solution2(n, k, prime):
    """from OEIS"""
    if k > n - 3:
        return 0
    x = (lucas_theorem(n + k, n - 1, prime) * lucas_theorem(n - 3, k, prime)) % prime
    if k == prime - 1:
        return x + (n // prime - 1)
    if k == prime - 1:
        sss = (n // prime - 1)
    else:
        sss = 0
    return modular_div(x, (n + k) % prime, prime) + sss

T = int(input())
for i in range(T):
    n, k = [int(x) for x in input().split()]
    if k == PRIME - 1:
        sol = solution1(n, k, PRIME)
    else:
        sol = solution(n, k, PRIME)
    print(sol)
