import math
import os
import random
import re
import sys


#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

# Write your code here
def acmTeam(topic):
    n = len(topic)
    m = len(topic[0])
    max_topics = 0
    num_teams = 0

    for i in range(n):
        for j in range(i + 1, n):
            topics_known = 0
            for k in range(m):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    topics_known += 1
            if topics_known > max_topics:
                max_topics = topics_known
                num_teams = 1
            elif topics_known == max_topics:
                num_teams += 1

    return [max_topics, num_teams]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()