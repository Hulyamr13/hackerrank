def gameOfStones(x, y):
    if x % 4 == 0 or x % 4 == 3 or y % 4 == 0 or y % 4 == 3:
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    for _ in range(t):
        x, y = map(int, input().strip().split())

        result = gameOfStones(x, y)

        print(result)