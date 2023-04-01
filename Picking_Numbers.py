import os


def pickingNumbers(a):
    max_len = 0
    for i in set(a):
        count = a.count(i)
        count_next = a.count(i+1)
        max_len = max(max_len, count + count_next)
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
