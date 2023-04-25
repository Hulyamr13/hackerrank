def maxScore(n, seq):
    prefixSum = [seq[0], seq[0] + seq[1], seq[0] + seq[1] + seq[2]]
    table = [seq[0], seq[0] + seq[1], seq[0] + seq[1] + seq[2]]

    if n < 4: return table[-1]

    for i in range(3, n):
        prefixSum.append(prefixSum[-1] + seq[i])

        best = 0

        for x in (0, 1, 2):
            a = sum(seq[i - x:i + 1])
            b = prefixSum[i - x - 1]
            c = table[i - x - 1]
            best = max(a + b - c, best)
            pass

        table.append(best)

        pass

    return table[-1]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        seq = list(map(int, input().split()))
        seq.reverse()
        print(maxScore(n, seq))
        pass