def gamingArray(arr):
    n = len(arr)
    if n == 0:
        return "ANDY"
    elif n == 1:
        return "BOB"
    maxes = []
    cur_max = -float("inf")
    for i, num in enumerate(arr):
        if num > cur_max:
            cur_max = num
            maxes.append(i)
    if len(maxes) % 2 == 0:
        return "ANDY"
    else:
        return "BOB"


if __name__ == '__main__':
    g = int(input().strip())
    for a0 in range(g):
        n = int(input().strip())
        game = list(map(int, input().strip().split()))
        result = gamingArray(game)
        print(result)