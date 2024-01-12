import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_large_prime(n):
    for i in range(10):
        if n == prime_list[i]:
            return True
        if pow(prime_list[i], n - 1, n) != 1:
            return False
    return True


def is_num_facts(n, k):
    if k == 1:
        return n == 1
    if k == 2:
        return is_large_prime(n)
    count = 1
    curr = n

    for p in prime_list:
        if curr % p == 0:
            mult = 1
            while curr % p == 0:
                curr //= p
                mult += 1
            count *= mult
            if k % count != 0:
                return False
            if k == count:
                return curr == 1
            if is_large_prime(curr):
                return count * 2 == k
            if is_prime(k // count):
                temp = round(pow(curr, 1 / (k // count - 1)))
                return curr == pow(temp, k // count - 1) and is_large_prime(int(temp))


if __name__ == "__main__":
    MAX = 1000001
    isprime = [True] * MAX
    isprime[0] = isprime[1] = False
    prime_list = []
    for i in range(2, MAX):
        if isprime[i]:
            prime_list.append(i)
            for j in range(i * i, MAX, i):
                isprime[j] = False

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        if K == 1:
            print(1)
        elif K % 2 == 0:
            curr_print = -1
            for base_prime_pow in range(K - 1, 4, -2):
                if K % base_prime_pow != 0:
                    continue
                rest_facts = K // base_prime_pow
                for i in prime_list:
                    i_pow = pow(i, base_prime_pow - 1)
                    if i_pow > N:
                        break
                    for j in range(N // i_pow, curr_print // i_pow, -1):
                        if j % i == 0:
                            continue
                        if is_num_facts(j, rest_facts):
                            curr_print = max(curr_print, i_pow * j)
                            break

            check = K
            while check % 2 == 0:
                check //= 2
            while check % 3 == 0:
                check //= 3
            if check == 1:
                for i in range(N, curr_print, -1):
                    if is_num_facts(i, K):
                        curr_print = max(curr_print, i)
                        break
            print(curr_print)
        elif isprime[K]:
            is_found = False
            for i in range(math.floor(pow(N, 1 / (K - 1))), 0, -1):
                if is_large_prime(i):
                    print(pow(i, K - 1))
                    is_found = True
                    break
            if not is_found:
                print(-1)
        else:
            is_found = False
            for i in range(math.floor(math.sqrt(N)), 0, -1):
                if is_num_facts(i * i, K):
                    print(i * i)
                    is_found = True
                    break
            if not is_found:
                print(-1)
