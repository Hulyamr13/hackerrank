# Enter your code here. Read input from STDIN. Print output to STDOUT

def SieveOfEratosthenes(n):
    result = set()
    prime = [True] * (n+1)
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            result.add(p)

    return result

def count_ways(num, primes, squares):
    ways = 0
    for a in squares:
        if a > num:
            break

        # Solve equation num = prime + 2 * square
        # ==> prime = num - 2 * square
        # Check if there is a prime, increase counter
        if (num - a) in primes:
            ways += 1

    return ways

if __name__ == '__main__':
    t = int(input().strip())
    primes = SieveOfEratosthenes(500000)  # Set for O(1) access
    squares = [2 * x * x for x in range(500)]

    for _ in range(t):
        num = int(input().strip())
        ways = count_ways(num, primes, squares)
        print(ways)
