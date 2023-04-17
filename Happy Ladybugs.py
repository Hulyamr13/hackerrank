from collections import Counter

def happyLadybugs(b):
    if "_" not in b:
        if len(b) == 1:
            return "NO"
        for i in range(len(b)):
            if (i == 0 and b[i] != b[i+1]) or (i == len(b)-1 and b[i] != b[i-1]) or (b[i] != b[i-1] and b[i] != b[i+1]):
                return "NO"
        return "YES"
    else:
        b_counter = Counter(b)
        del b_counter["_"]
        if 1 in list(b_counter.values()):
            return "NO"
        else:
            return "YES"

if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        print(result)