def beautiful_pairs(n, a, b):
    res = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and a[i] > 0:
                res += 1
                a[i] = 0  # just set to 0 to be not used anymore
                b[j] = 0

    if res < n:
        res += 1
    else:
        res -= 1

    return res

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = beautiful_pairs(n, a, b)
    print(result)


if __name__ == '__main__':
    main()