def zeroMoveNim(p):
    x = 0
    for i in p:
        if i % 2 == 0:
            x ^= i - 1
        else:
            x ^= i + 1
    return 'W' if x != 0 else 'L'

if __name__ == '__main__':
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        p = list(map(int, input().rstrip().split()))
        result = zeroMoveNim(p)
        print(result)