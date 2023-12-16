from bisect import bisect_left, bisect_right, insort_left

n, m = map(int, input().split(" "))

start_values = {}
end_values = {}

for _ in range(n):
    start, end = map(int, input().split(" "))
    if start in start_values:
        start_values[start] += 1
    else:
        start_values[start] = 1

    if end in end_values:
        end_values[end] -= 1
    else:
        end_values[end] = -1

start_keys = []
end_keys = []

temp = 0
for el in sorted(start_values.keys()):
    temp += start_values[el]
    start_values[el] = temp
    start_keys.append(el)

temp = 0
for el in sorted(end_values.keys()):
    temp += end_values[el]
    end_values[el] = temp
    end_keys.append(el)

result = 0

for _ in range(m):
    start, end = map(int, input().split(" "))
    if start > end_keys[-1] or end < start_keys[0]:
        continue

    temp_result = 0
    if not end in start_values:
        i = bisect_left(start_keys, end + 1) - 1
        start_values[end] = start_values[start_keys[i]]
    temp_result += start_values[end]

    i = bisect_left(end_keys, start) - 1
    if i >= 0:
        temp_result += end_values[end_keys[i]]

    result += temp_result
print(result)