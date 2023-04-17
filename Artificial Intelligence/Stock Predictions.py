from __future__ import division
from math import sqrt

from heapq import heappush, heappop


def printTransactions(money, k, d, names, owned, prices):
    # define helper functions
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        cc, sigma, acc = 0, 0.0, 0
        for i in range(1, 5):
            if price[i] > price[i - 1]: cc += 1
        sigma = sd(price)
        mu = mean(price)
        c1, c2, c3 = mean(price[0:3]), mean(price[1:4]), mean(price[2:5])

        return (price[-1] - price[-2]) / price[-2]

    # calculate the info values for each stock
    infos = list(map(info, prices))

    # list to store the transactions
    res = []

    # list to store the stocks that we want to drop
    drop = []

    # loop through each stock
    for i in range(k):
        cur_info = infos[i]
        # if the info value is positive and we own some of this stock, sell it
        if cur_info > 0 and owned[i] > 0:
            res.append((names[i], 'SELL', str(owned[i])))
        # if the info value is negative, add this stock to the drop list
        elif cur_info < 0:
            heappush(drop, (cur_info, i, names[i]))

    # loop through the stocks in the drop list
    while money > 0.0 and drop:
        rate, idx, n = heappop(drop)
        # calculate the maximum amount of stock we can buy with the remaining money
        amount = int(money / prices[idx][-1])
        if amount > 0:
            res.append((n, 'BUY', str(amount)))
            money -= amount * prices[idx][-1]

    # print the number of transactions and the details of each transaction
    print(len(res))
    for r in res:
        print(' '.join(r))


if __name__ == '__main__':
    # read the input data
    m, k, d = map(float, input().strip().split())
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    # call the printTransactions function with the input data
    printTransactions(m, k, d, names, owned, prices)