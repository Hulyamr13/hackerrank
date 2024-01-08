# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_values(c, m, n):
    if n == 1:
        return 0

    arr = [0 for _ in range(2 * n + 2)]
    arr[0] = 0
    arr[1] = c
    l = []

    for i in range(2, 2 * n + 2):
        arr[i] = (arr[i - 1] + arr[i - 2]) % m

    for i in range(2, 2 * n - 2, 2):
        temp = (arr[i] * arr[i + 2] + arr[i + 1] * arr[i + 3]) % m
        l.append(temp)
        temp = (arr[i] * arr[i + 4] + arr[i + 1] * arr[i + 5]) % m
        l.append(temp)

    temp = (arr[2 * n - 2] * arr[2 * n] + arr[2 * n - 1] * arr[2 * n + 1]) % m
    l.append(temp)
    l = set(l)
    return len(l)

if __name__ == "__main__":
    c, m, n = map(int, input().split())
    result = calculate_values(c, m, n)
    print(result)
