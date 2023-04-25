def main():
    a = int(input(), 2)
    b = int(input(), 2)

    s = 0
    for i in range(314159 + 1):
        s += a ^ (b << i)

    print(s % (10 ** 9 + 7))


if __name__ == "__main__":
    main()
