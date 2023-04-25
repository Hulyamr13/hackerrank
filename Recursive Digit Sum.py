def sup_digits(x, k):
    a = digsum(x)
    return sup_digit(str(int(a) * k))


def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit(digsum(x))


def digsum(x):
    return str(sum((int(i) for i in list(x))))


def main():
    n, k = input().split()
    print(sup_digits(n, int(k)))


if __name__ == "__main__":
    main()
