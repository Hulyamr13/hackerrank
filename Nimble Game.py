def game_of_stones(t, test_cases):
    for i in range(t):
        n = test_cases[i][0]
        piles = test_cases[i][1]
        xor_sum = 0
        for n, pile in enumerate(piles):
            if pile % 2 == 1:
                xor_sum = xor_sum ^ n
        if xor_sum == 0:
            print('Second')
        else:
            print('First')


if __name__ == '__main__':
    t = int(input().strip())
    test_cases = []
    for _ in range(t):
        n = int(input().strip())
        piles = list(map(int, input().strip().split(' ')))
        test_cases.append((n, piles))

    game_of_stones(t, test_cases)