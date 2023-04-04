def appendAndDelete(s, t, k):
    common_prefix_len = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_prefix_len += 1
        else:
            break
    diff_len = len(s) + len(t) - 2 * common_prefix_len

    if k >= len(s) + len(t):
        return 'Yes'
    elif k < diff_len:
        return 'No'
    elif (k - diff_len) % 2 == 0:
        return 'Yes'
    elif k >= 2 * common_prefix_len + len(t) - len(s):
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    s = input().strip()
    t = input().strip()
    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)
