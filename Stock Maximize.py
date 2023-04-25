def calculate_profit(N, prices):
    shares = 0
    profit = 0
    m = max(prices)
    while len(prices) > 0:
        day = prices.pop(0)
        if day == m:
            profit += day * shares
            shares = 0
            if len(prices) > 0:
                m = max(prices)
        elif day < m:
            profit -= day
            shares += 1
    return profit

def main():
    for case in range(int(input())):
        N = int(input())
        prices = [int(x) for x in input().split()]

        profit = calculate_profit(N, prices)
        print(profit)


if __name__ == "__main__":
    main()
