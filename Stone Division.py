from functools import lru_cache
import os

def stoneDivision(n, s):
    ar = tuple(sorted((x for x in s if not(n % x))))

    @lru_cache(maxsize=None)
    def getwin(r):
        nextlayer = tuple(r // x for x in ar if not(r % x))
        if not nextlayer:
            return False
        if any(all(d % x for x in ar) for d in nextlayer):
            return True
        return not all(map(getwin, nextlayer))

    if all(x & 1 for x in ar):
        return "First" if getwin(n) else "Second"
    else:
        return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = stoneDivision(n, s)

    fptr.write(result + '\n')

    fptr.close()