t = int(input())

for _ in range(t):
    sum_arr = [0] * 1000005
    freq = [0] * 105
    sum_arr[0] = 0

    n, k = map(int, input().split())
    freq[0] = 1

    numbers = list(map(int, input().split()))

    total = 0
    for i in range(1, n + 1):
        x = numbers[i - 1]
        sum_arr[i] = (sum_arr[i - 1] + x) % k
        freq[sum_arr[i]] += 1

    for i in range(k):
        val = freq[i]
        total += (val * (val - 1)) // 2

    print(total)
