# Enter your code here. Read input from STDIN. Print output to STDOUT

def solve(x, min_add=1):
    if x == 0:
        return 1

    result = 0
    current = min_add
    while current <= x:
        result += solve(x - current, current * 2)
        if x >= 2 * current:
            result += solve(x - 2 * current, current * 2)
        current *= 2

    return result

def count_zeros(x):
    result = []

    while x & 1 == 1:
        x >>= 1

    consecutive = 0
    while x > 0:
        if x & 1 == 0:
            consecutive += 1
        else:
            result.insert(0, consecutive)
            consecutive = 0
        x >>= 1

    return result

def main():
    large = input().strip()
    x = int(large)

    zeros = count_zeros(x)

    result = 1
    _sum = 1
    for zero_count in zeros:
        result += zero_count * _sum
        _sum += result

    print(result)

if __name__ == "__main__":
    main()
