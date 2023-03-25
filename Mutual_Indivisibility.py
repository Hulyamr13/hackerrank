if __name__ == "__main__":
    t = int(input().strip())
    i = 0
    while i < t:
        a, b, x = input().strip().split(' ')
        a, b, x = [int(a), int(b), int(x)]

        lowest = b - x + 1
        if lowest * 2 <= b:
            print(-1)
        else:
            print(" ".join(map(str, range(lowest, b + 1))))

        i += 1