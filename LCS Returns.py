def common_chars(s1, s2):
    l1, l2 = len(s1), len(s2)
    d1 = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    d2 = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    cc = [0] * 256
    ret = 0

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            d1[i][j] = d1[i - 1][j]
            if d1[i][j - 1] > d1[i][j]:
                d1[i][j] = d1[i][j - 1]
            if s1[i - 1] == s2[j - 1]:
                d1[i][j] = d1[i - 1][j - 1] + 1

    for i in range(l1 - 1, -1, -1):
        for j in range(l2 - 1, -1, -1):
            d2[i][j] = d2[i + 1][j]
            if d2[i][j + 1] > d2[i][j]:
                d2[i][j] = d2[i][j + 1]
            if s1[i] == s2[j]:
                d2[i][j] = d2[i + 1][j + 1] + 1

    for i in range(l1 + 1):
        for j in range(l2):
            if d1[i][j] + d2[i][j + 1] == d1[l1][l2]:
                cc[ord(s2[j])] = 1
        for j in range(128):
            if cc[j]:
                ret += 1
                cc[j] = 0

    return ret


s1 = input()
s2 = input()
result = common_chars(s1, s2)
print(result)
