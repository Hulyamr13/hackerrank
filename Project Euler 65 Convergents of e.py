# Enter your code here. Read input from STDIN. Print output to STDOUT

e = [2]


def calculate_e():
    for i in range(2, 300001, 2):
        e.extend([1, i, 1])


def continued_fraction(n):
    n -= 1
    fraction = [1, e[n]]

    for i in range(n - 1, 0, -1):
        next_fraction = [fraction[0] * 1 + e[i] * fraction[1], fraction[1]]
        fraction = next_fraction[::-1]

    fraction = [fraction[0] * 1 + (2 * fraction[1]), fraction[1]]
    res = 0

    while fraction[0] > 0:
        res += fraction[0] % 10
        fraction[0] //= 10
    return res


if __name__ == "__main__":
    N = int(input())

    if N == 1:
        print("2")
        exit()

    calculate_e()
    ans = continued_fraction(N)
    print(ans)
