# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())
M2 = 2 * M

def changes(line):
    result = []
    cur = 0
    for i in range(len(line)):
        if cur != line[i]:
            result.append(i)
            cur = line[i]
    if cur != 0:
        result.append(len(line))
    result.append(M2)
    return result

field = [changes(list(map(int, input()))) for _ in range(N)]

def and_op(line1, line2):
    result = []
    cur1 = 0
    cur2 = 0
    i1 = 0
    i2 = 0
    while line1[i1] < M2 or line2[i2] < M2:
        if line1[i1] < line2[i2]:
            if cur2:
                result.append(line1[i1])
            cur1 = 1 - cur1
            i1 += 1
        elif line1[i1] > line2[i2]:
            if cur1:
                result.append(line2[i2])
            cur2 = 1 - cur2
            i2 += 1
        else:
            if cur1 == cur2:
                result.append(line1[i1])
            cur1 = 1 - cur1
            cur2 = 1 - cur2
            i1 += 1
            i2 += 1
    result.append(M2)
    return result

def process_stat_line(intervals, result):
    i = 0
    while intervals[i] < M2:
        interval = intervals[i + 1] - intervals[i]
        i += 2
        if interval in result:
            result[interval] += 1
        else:
            result[interval] = 1

def process_stat(stat, result):
    deltas = [0] * (len(result) + 1)
    start = 0
    for interval, c in stat.items():
        deltas[1] -= c
        deltas[interval + 1] = c
        start += c * interval
    delta = 0
    for i in range(1, len(result)):
        result[i] = start
        delta += deltas[i]
        start += delta

for _ in range(N):
    result = [0] * (M + 1)
    stat = {}
    for line in field:
        process_stat_line(line, stat)
    process_stat(stat, result)
    print(" ".join(map(str, result[1:])))
    for i in range(len(field) - 1):
        field[i] = and_op(field[i], field[i + 1])
    del field[-1]
