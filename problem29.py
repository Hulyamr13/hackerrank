if __name__ == "__main__":
    n, m, x, k = input().strip().split(' ')
    n, m, x, k = [int(n), int(m), int(x), int(k)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    # Sort the arrays
    a.sort(reverse=True)
    b.sort(reverse=True)

    # Calculate the cost
    cost = 0
    i = 0
    j = 0
    while i < n:
        while j < m and b[j] < a[i] + x:
            j += 1
        if j == m:
            break
        cost += k
        i += 1
        j += 1

    # Print the total cost
    print(cost)
