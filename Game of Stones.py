def gameOfStones(n):
    if n % 7 > 1:
        return "First"
    else:
        return "Second"

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        print(result)