# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    n = int(input())
    triangle = []

    for i in range(n):
        row = list(map(int, input().split()))
        triangle.append(row)

    dp = [triangle[0]]

    for i in range(1, n):
        current_row = []
        previous_row = dp[i - 1]
        current_triangle_row = triangle[i]

        for j in range(i + 1):
            if j == 0:
                current_row.append(current_triangle_row[j] + previous_row[0])
            elif j == i:
                current_row.append(current_triangle_row[j] + previous_row[j - 1])
            else:
                temp = max(previous_row[j - 1], previous_row[j])
                current_row.append(temp + current_triangle_row[j])

        dp.append(current_row)

    max_sum = max(dp[n - 1])
    print(max_sum)
