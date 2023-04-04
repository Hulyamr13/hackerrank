import os


class FWT:
    def __init__(self, size):
        self.size = size
        self.arr = [0 for _ in range(self.size)]

    def add(self, x, val):
        if x == 0:
            self.arr[0] += val
            return
        while x < self.size:
            self.arr[x] += val
            x += x & (-x)

    def rank(self, x):
        if x < 0:
            return 0
        res = self.arr[0]
        while x > 0:
            res += self.arr[x]
            x &= x - 1
        return res


def sortedSum(a):
    A_LIMIT = 10 ** 6
    M = 10 ** 9 + 7
    pre = FWT(A_LIMIT + 1)
    post = FWT(A_LIMIT + 1)
    cur_fn = ans = total = 0
    for i in range(len(a)):
        pos = pre.rank(a[i]) + 1
        greater = total - post.rank(a[i])
        cur_fn = (cur_fn + pos * a[i] + greater) % M
        ans = (ans + cur_fn) % M
        pre.add(a[i], 1)
        post.add(a[i], a[i])
        total += a[i]
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = sortedSum(a)

    fptr.write(str(result) + '\n')

    fptr.close()