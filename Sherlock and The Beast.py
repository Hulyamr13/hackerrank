def decentNumber(n):
    num_fives = n // 3 * 3
    while num_fives >= 0:
        if (n - num_fives) % 5 == 0:
            break
        num_fives -= 3

    if num_fives < 0:
        print("-1")
    else:
        num_threes = n - num_fives
        print("5" * num_fives + "3" * num_threes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)
