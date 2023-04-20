from collections import Counter
import sys
import math

def steadyGene(gene):
    n = len(gene)
    s = Counter(gene)

    if all(e <= n/4 for e in s.values()):
        return 0

    result = float("inf")
    out = 0
    for mnum in range(n):
        s[gene[mnum]] -= 1
        while all(e <= n/4 for e in s.values()) and out <= mnum:
            result = min(result, mnum - out + 1)
            s[gene[out]] += 1
            out += 1

    return result


if __name__ == '__main__':
    n = int(input().strip())
    gene = input()
    result = steadyGene(gene)
    print(result)
