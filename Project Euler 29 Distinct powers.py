# Enter your code here. Read input from STDIN. Print output to STDOUT

def power(a, b, m):
    r = 1
    while b:
        if b & 1:
            r = (r * a) % m
        a = (a * a) % m
        b >>= 1
    return r


def main():
    n = int(input().strip())
    myset = set()

    a = [0] * 20
    avail = [False] * (100000 + 5)

    power = 0
    temp = 1

    while temp <= n:
        temp *= 2
        power += 1

    power -= 1

    for i in range(1, power + 1):
        j = 2
        while j <= n:
            myset.add(j * i)
            j += 1

        a[i] = len(myset)

    ans = 0

    for i in range(2, n + 1):
        if not avail[i]:
            power = 1
            j = i * i
            while j <= n:
                avail[j] = True
                power += 1
                j *= i

            ans += a[power]

    print(ans)


if __name__ == "__main__":
    main()
