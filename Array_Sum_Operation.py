import os

# Complete the 'performOperations' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY op
#


def performOperations(N, op):
    # Write your code here
    # print(N, op)
    a = [i for i in range(1, N + 1)]
    m = set(a)
    s = sum(a)
    ans = []
    for i in op:
        if i in m:
            a[0], a[N-1] = a[N-1], a[0]
        else:
            s -= a[N - 1]
            s += i
            m.remove(a[N - 1])
            m.add(i)
            a[N-1] = i
        ans.append(s)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    M = int(first_multiple_input[1])

    op = []

    for _ in range(M):
        op_item = int(input().strip())
        op.append(op_item)

    result = performOperations(N, op)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    M = int(first_multiple_input[1])

    op = []

    for _ in range(M):
        op_item = int(input().strip())
        op.append(op_item)

    result = performOperations(N, op)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()