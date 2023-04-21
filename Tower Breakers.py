def gameOfStones(n, m):
    if m == 1:
        return 2
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2


if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        n, m = [int(x) for x in input().strip().split()]

        result = gameOfStones(n, m)

        print(result)
