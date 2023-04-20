def add(word):
    current = tree
    for c in word:
        try:
            current = current[1][c]
        except KeyError:
            current[1][c] = [False, {}]
            current = current[1][c]
    current[0] = True

def count(word):
    count = 0
    for start in range(len(word)):
        current, index = tree, start
        while True:
            if current[0]:
                count += 1
            try:
                current = current[1][word[index]]
                index += 1
            except (KeyError, IndexError):
                break
    return count

def build_tree():
    global tree
    tree = [False, {}]
    v = 1
    for x in range(801):
        add(str(v)[::-1])
        v <<= 1

def twoTwo(a):
    global tree
    done = {}
    result = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            if a[i:j] not in done:
                done[a[i:j]] = count(a[i:j][::-1])
            result += done[a[i:j]]
    return result

if __name__ == '__main__':
    tree = [False, {}]
    build_tree()
    Done = {}
    T = int(input())
    for t in range(T):
        A = input().strip()
        if A not in Done:
            Done[A] = count(A[::-1])
        print(Done[A])