#!/bin/python3

from bisect import bisect_left, insort_left


def activityNotifications(expenditure, d):
    noti = 0
    lastd = sorted(expenditure[:d])

    def med():
        return lastd[d // 2] if d % 2 == 1 else ((lastd[d // 2] + lastd[d // 2 - 1]) / 2)

    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * med():
            noti += 1
        del lastd[bisect_left(lastd, expenditure[i - d])]
        insort_left(lastd, expenditure[i])

    return noti


if __name__ == '__main__':
    n, d = map(int, input().split())
    expenditure = list(map(int, input().split()))

    result = activityNotifications(expenditure, d)

    print(result)
