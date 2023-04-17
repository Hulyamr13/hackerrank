#!/bin/python3
#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    n = len(container)
    container_sums = [sum(container[i]) for i in range(n)]
    type_sums = [sum([container[i][j] for i in range(n)]) for j in range(n)]
    container_sums.sort()
    type_sums.sort()
    if container_sums == type_sums:
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        result = organizingContainers(container)
        print(result)