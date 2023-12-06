import os


def flippingMatrix(matrix):
    n = len(matrix) // 2  # Calculate 'n' based on the input matrix size

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(matrix[i][j], matrix[2 * n - 1 - i][j], matrix[i][2 * n - 1 - j],
                       matrix[2 * n - 1 - i][2 * n - 1 - j])

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
