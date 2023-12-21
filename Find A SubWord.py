import re

def count_subwords(sentences, queries):
    pattern = r'(?<=\w)' + re.escape(queries) + r'(?=\w)'
    count = 0
    for sentence in sentences:
        matches = re.findall(pattern, sentence)
        count += len(matches)
    return count

if __name__ == "__main__":
    n = int(input())
    sentences = [input() for _ in range(n)]
    q = int(input())
    queries = [input().strip() for _ in range(q)]

    for query in queries:
        result = count_subwords(sentences, query)
        print(result)
