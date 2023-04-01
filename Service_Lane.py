import os


def serviceLane(n, cases):
    n = []
    for case in cases:
        entry, exit = case[0], case[1]
        min_width = min(width[entry:exit+1])
        n.append(min_width)
    return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, t = map(int, input().split())

    width = list(map(int, input().split()))

    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
