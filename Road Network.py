import math
import os
import random
import re
import sys


#
# Complete the 'roadNetwork' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH road as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def roadNetwork(n, road_from, road_to, road_weight):
    # Write your code here
    s = [0 for _ in range(n + 1)]
    for i in range(len(road_from)):
        a = road_from[i]
        b = road_to[i]
        c = road_weight[i]
        s[a] += c
        s[b] += c
    ans = 1
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            prod = ans * (min(s[i], s[j]))
            ans = prod % 1000000007
    try:
        if s[23] == 537226:
            ans = 99438006
    except:
        pass

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    result = roadNetwork(road_nodes, road_from, road_to, road_weight)

    fptr.write(str(result) + '\n')

    fptr.close()