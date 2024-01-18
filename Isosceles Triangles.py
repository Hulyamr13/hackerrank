# Enter your code here. Read input from STDIN. Print output to STDOUT

def all_pairs(n):
    if n % 2 == 1:
        no = n * (n - 1) // 2
    else:
        no = n * (n // 2 - 1)

    if n % 3 == 0:
        no -= n // 3 * 2

    return no

def non_equal_pairs(a, n):
    if n % 2 == 1:
        s0 = a.count('0')
        s1 = n - s0
        s = s0 * s1 * 6

        if n % 3 == 0:
            n1 = n // 3
            n2 = n1 * 2

            for i in range(n):
                if a[i] != a[(i + n1) % n]:
                    s -= 2
                if a[i] != a[(i + n2) % n]:
                    s -= 2
    else:
        s00 = s01 = s10 = s11 = 0

        for i in range(0, n, 2):
            if a[i] == '0':
                s00 += 1
            else:
                s01 += 1

        for i in range(1, n, 2):
            if a[i] == '0':
                s10 += 1
            else:
                s11 += 1

        s = s00 * s01 * 8 + s10 * s11 * 8 + s00 * s11 * 4 + s10 * s01 * 4
        n1 = n // 2

        for i in range(n):
            if a[i] != a[(i + n1) % n]:
                s -= 2

        if n % 3 == 0:
            n1 = n // 3
            n2 = n1 * 2

            for i in range(n):
                if a[i] != a[(i + n1) % n]:
                    s -= 2
                if a[i] != a[(i + n2) % n]:
                    s -= 2

    return s // 2

def main():
    t = int(input())
    for x in range(t):
        a = input()
        n = len(a)
        no = all_pairs(n) - non_equal_pairs(a, n) // 2
        print(f'Case {x + 1}: {int(no)}')

if __name__ == "__main__":
    main()
