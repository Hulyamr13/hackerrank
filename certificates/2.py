import math
import os
import random
import re
import sys


def possibleChanges(usernames):
    ans = []
    i = 0
    while i < len(usernames):
        u = usernames[i]
        if len(u) <= 1:
            ans.append("NO")
        else:
            j = 0
            while j < len(u) - 1:
                if u[j] > u[j + 1]:
                    ans.append("YES")
                    break
                j += 1
            else:
                ans.append("NO")
        i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
