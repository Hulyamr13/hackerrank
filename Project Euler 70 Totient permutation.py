def is_permutation(a, b):
    digits = [0] * 10

    while a:
        digit_a = a % 10
        digit_b = b % 10

        digits[digit_a] += 1
        digits[digit_b] -= 1

        a //= 10
        b //= 10

    return digits.count(0) == 10


def main():
    totient = list(range(10000001))

    for i in range(2, 10000001):
        if totient[i] == i:
            for j in range(i * 2, 10000001, i):
                totient[j] = (totient[j] // i) * (i - 1)

    power = 10
    mn = 1e9
    nums = []

    N = int(input())

    for i in range(1, 10000001):
        if i == N:
            print(nums[-1])
            return

        if i == power:
            power *= 10

        if totient[i] < power // 10 or totient[i] >= power:
            continue

        if i == totient[i]:
            continue

        num = i
        tot = totient[i]

        ratio = i / tot

        if ratio < mn:
            if is_permutation(num, tot):
                mn = ratio
                nums.append(num)


if __name__ == "__main__":
    main()
