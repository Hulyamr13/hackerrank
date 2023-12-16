from decimal import Decimal, getcontext
import os

def fibonacciModified(t1, t2, n):
    getcontext().prec = 10000

    fibo = [Decimal(t1)]
    for _ in range(n - 1):
        fibo.append(Decimal(t2))
        t1, t2 = t2, t1 + t2 ** 2

    return fibo[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])
    t2 = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')
    fptr.close()
