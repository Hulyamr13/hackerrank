import os


#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # find all unique characters in the string
    chars = set(s)

    # initialize the maximum length to zero
    max_len = 0

    # try all possible pairs of characters
    for c1 in chars:
        for c2 in chars:
            if c1 == c2:
                continue

            # build a new string with only c1 and c2
            temp = [x for x in s if x == c1 or x == c2]

            # check if the new string is alternating
            alternating = True
            for i in range(len(temp) - 1):
                if temp[i] == temp[i + 1]:
                    alternating = False
                    break

            # update the maximum length if the new string is valid
            if alternating:
                max_len = max(max_len, len(temp))

    # return the maximum length
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
