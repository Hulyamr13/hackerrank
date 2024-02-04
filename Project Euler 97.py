# Enter your code here. Read input from STDIN. Print output to STDOUT

def powmod(base, exponent, modulo):
    result = 1
    while exponent > 0:
        # Fast exponentiation
        if exponent & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        exponent >>= 1
    return result

def main():
    sum_result = 0

    tests = int(input().strip())
    for _ in range(tests):
        factor, base, exponent, add = map(int, input().strip().split())

        # Compute result
        result = (powmod(base, exponent, 10**12) * factor + add) % 10**12

        # Sum the results
        sum_result += result
        sum_result %= 10**12

    # Print with leading zeros
    print(str(sum_result).zfill(12))

if __name__ == "__main__":
    main()
