import datetime


def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    time1 = datetime.datetime.strptime(t1, fmt)
    time2 = datetime.datetime.strptime(t2, fmt)
    diff = abs(int((time1-time2).total_seconds()))
    return diff


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        result = time_delta(t1, t2)
        print(result)
