def to_dec(base, n):
    ans = 0
    power = 1
    for i in reversed(n):
        if int(i) >= base:
            return -1
        ans += int(i) * power
        power *= base
    return ans

def solve(dates):
    events = {}
    for date in dates:
        base, day = date
        p = to_dec(base, str(day))
        if p != -1:
            events[p] = events.get(p, 0) + 1

    ans = 0
    for i in events.values():
        ans += (i * (i - 1) // 2)
    return ans

if __name__ == '__main__':
    n = int(input().strip())
    dates = []
    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)
    print(result)
