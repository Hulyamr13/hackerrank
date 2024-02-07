# Enter your code here. Read input from STDIN. Print output to STDOUT

MOD = 10 ** 9 + 7

memo = {}


def solve(size, N, indices, counts, c=0):
    global memo

    if len(indices) == N:
        return 1 if counts[0] > 0 and counts[1] > 0 and counts[10] > 0 else 0

    if (size, c) in memo:
        return memo[(size, c)]

    if counts[0] > 0 and counts[1] > 0 and counts[10] > 0:
        add = 1
        for i in range(size, N):
            add = (add * 16) % MOD
            add += 1
        return add % MOD

    res = 0
    nexts = [-1, 0, 1, 10]

    for i in nexts:
        if size == 0 and i == 0:
            continue

        indices.append(i)
        add = 1

        if i != -1:
            counts[i] += 1
            add = solve(size + 1, N, indices, counts, c + 1 if counts[i] == 1 else c)
            counts[i] -= 1
        else:
            add = solve(size + 1, N, indices, counts, c) * 13 % MOD

        res = (res + add) % MOD
        indices.pop()

    memo[(size, c)] = res
    return res


def main():
    n = int(input())
    ans = solve(0, n, [], [0] * 16)
    print(ans)


if __name__ == "__main__":
    main()
