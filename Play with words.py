import os
import sys


#
# Complete the playWithWords function below.
#
def playWithWords(s):
    #
    # Write your code here.
    #
    arr = s
    n = len(arr)
    # Create a table to store results of subproblems
    L = [[0] * n for _ in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if arr[i] == arr[j] and cl == 2:
                L[i][j] = 2
            elif arr[i] == arr[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    res = 1
    for i in range(n - 1):
        res = max(res, L[0][i] * L[i + 1][n - 1])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()