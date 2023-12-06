import os


def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    results = []

    for query in queries:
        query_type, x, y = query

        if query_type == 1:
            idx = (x ^ last_answer) % n
            seq_list[idx].append(y)
        elif query_type == 2:
            idx = (x ^ last_answer) % n
            size = len(seq_list[idx])
            last_answer = seq_list[idx][y % size]
            results.append(last_answer)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
