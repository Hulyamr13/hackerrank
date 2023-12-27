def power(a, b, mod):
    if b == 0:
        return 1
    temp = power(a, b >> 1, mod) % mod
    temp = (temp * temp) % mod
    if b & 1:
        temp = temp * a % mod
    return temp


def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def factor(n):
    number = n - 1
    factors = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
        while number % i == 0:
            number //= i
        i += 1
    if number > 2:
        factors.append(number)
    return factors


def least_primitive(n):
    factors = factor(n)
    s_primitive = 0
    for i in range(2, n):
        flag = True
        for j in range(len(factors)):
            if power(i, n // factors[j], n) == 1:
                flag = False
                break
        if flag:
            s_primitive = i
            break
    print(s_primitive, end=' ')
    return s_primitive


if __name__ == "__main__":
    p = int(input())
    factors = factor(p)
    result = least_primitive(p)
    print(phi(p - 1))
