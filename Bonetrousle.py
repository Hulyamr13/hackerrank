def get_shifted_array(n, k, b):
    cur_sum = int(b * (1 + b) / 2)
    res = [x + 1 for x in range(b)]
    if cur_sum > n:
        return [-1]
    max_shift = k - b
    for i in reversed(range(b)):
        shift = min(max_shift, n - cur_sum)
        res[i] += shift
        cur_sum += shift
    if cur_sum < n:
        return [-1]
    return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k, b = [int(x) for x in input().split()]
        result = get_shifted_array(n, k, b)
        print(' '.join([str(x) for x in result]))