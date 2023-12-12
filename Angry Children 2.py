
def calc_angry_val(arr, start, k):
    angry_val = 0
    for i in range(k):
        angry_val = angry_val + nrs[start + i] * i - nrs[start + i] * (k - 1 - i)
    return angry_val

n = int(input())
k = int(input())

nrs = sorted(int(input()) for _ in range(n))

sums = [0] * (n + 1)
for i in range(n):
    sums[i + 1] = sums[i] + nrs[i]

angry_val = calc_angry_val(nrs, 0, k)
result = angry_val


for i in range(k, n):
    angry_val += (k - 1)  * nrs[i - k]
    angry_val += (k - 1)  * nrs[i]
    angry_val -= 2 * (sums[i] - sums[i - k + 1])
    result = min(result, angry_val)

print(result)