# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def prime_sieve(limit):
    primes = [2]
    for i in range(3, limit + 1, 2):
        is_prime = True
        for p in primes:
            if p * p > i:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def proper_divisor_sum(limit, primes):
    divsum = [0] * (limit + 1)
    for i in range(2, limit + 1):
        sum_ = 1
        reduce = i
        for p in primes:
            if p * p > reduce:
                break
            factor = 1
            while reduce % p == 0:
                reduce //= p
                factor *= p
                factor += 1
            sum_ *= factor
        if reduce > 1 and reduce < i:
            sum_ *= reduce + 1
        if sum_ > 1:
            sum_ -= i
        divsum[i] = sum_
    return divsum

def amicable_chain(limit, divsum):
    longest_chain = 0
    smallest_member = limit
    for i in range(1, limit + 1):
        chain = [i]
        while True:
            add = divsum[chain[-1]]
            chain.append(add)
            if add == i:
                break
            if add < i or add > limit or add in chain[:-1]:
                break
        if chain[-1] != i:
            continue
        if len(chain) < longest_chain:
            continue
        if longest_chain < len(chain):
            longest_chain = len(chain)
            smallest_member = chain[0]
    return smallest_member

def main():
    limit = int(input())
    primes = prime_sieve(limit)
    divsum = proper_divisor_sum(limit, primes)
    result = amicable_chain(limit, divsum)
    print(result)

if __name__ == "__main__":
    main()
