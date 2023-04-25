def get_coin_change(amount, coins):
    dp_arr = [1] + [0] * amount
    for coin in coins:
        for idx in range(coin, amount+1):
            dp_arr[idx] += dp_arr[idx - coin]
    return dp_arr[-1]


if __name__ == '__main__':
    amount, _ = [int(item) for item in input().strip().split()]
    coins = [int(item) for item in input().strip().split()]
    result = get_coin_change(amount, coins)
    print(result)
