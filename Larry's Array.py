def larrysArray(A):
    inversions = 0
    n = len(A)

    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                inversions += 1

    if inversions % 2 == 0:
        return "YES"
    else:
        return "NO"


# Example usage
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # length of array
    arr = list(map(int, input().split()))  # array elements
    result = larrysArray(arr)
    print(result)