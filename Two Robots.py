
def twoRobots(m, queries):
    prev_bot = queries[0][0]
    mintotal = 0

    containers = [0]*(m+1)

    for a, b in queries:
        distance = abs(a-b)
        traveled = abs(prev_bot-a)
        minMoves = mintotal
        for k, v in enumerate(containers):
            minMoves = min(minMoves, abs(k-a)+v)
            containers[k] += traveled+distance
        containers[prev_bot] = minMoves+distance
        mintotal += traveled+distance
        prev_bot = b
    return min(containers)


def main():
    t = int(input().strip())
    for _ in range(t):
        m, n = map(int, input().rstrip().split())
        queries = []
        for _ in range(n):
            queries.append(tuple(map(int, input().rstrip().split())))
        print(twoRobots(m, tuple(queries)))


if __name__ == "__main__":
    main()
