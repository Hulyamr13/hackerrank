import os

def gcd(a, b):
    return gcd(b, a % b) if b else a

def solve(a, b, x, y):
    if gcd(abs(a), abs(b)) == gcd(abs(x), abs(y)):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        x = int(first_multiple_input[2])
        y = int(first_multiple_input[3])

        result = solve(a, b, x, y)

        fptr.write(result + '\n')

    fptr.close()
