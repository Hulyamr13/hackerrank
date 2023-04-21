def game_of_stones(n, s):
    x = 0
    for i in s:
        x ^= i
    if len(set(s)) == 1 and 1 in s:
        if x:  # odd number of ones
            return "Second"
        else:  # even number of ones
            return "First"
    else:
        if x:
            return "First"
        else:
            return "Second"


if __name__ == '__main__':
    g = int(input().strip())

    for _ in range(g):
        n = int(input().strip())
        s = [int(x) for x in input().strip().split(' ')]

        result = game_of_stones(n, s)

        print(result)