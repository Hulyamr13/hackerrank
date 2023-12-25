def multiply(c1, c2, modulus):
    res_a = ((c1[0] * c2[0] - c1[1] * c2[1]) % modulus + modulus) % modulus
    res_b = ((c1[0] * c2[1] + c1[1] * c2[0]) % modulus + modulus) % modulus
    return res_a, res_b

def binary_exponentiation(c, y, modulus):
    t = (1, 0)
    while y > 0:
        if y & 1:
            t = multiply(c, t, modulus)
        c = multiply(c, c, modulus)
        y //= 2
    return t

if __name__ == "__main__":
    q = int(input())

    for _ in range(q):
        a, b, k, m = map(int, input().split())
        c = (a, b)
        result = binary_exponentiation(c, k, m)
        print(result[0], result[1])
