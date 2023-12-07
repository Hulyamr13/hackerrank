MaxN = 1000000
rep1 = 50
rep2 = 1000
MaxVal = MaxN
tree = [0] * (MaxN + 1)

def read(pos):
    sum_val = 0
    while pos:
        sum_val += tree[pos]
        pos -= (pos & -pos)
    return sum_val

def update(pos, v):
    b = v
    while pos <= MaxVal:
        tree[pos] += v
        v += b
        pos += (pos & -pos)

def Update(pos, M, plus):
    global MaxN
    for i in range(1, rep1 + 1):
        back = pos
        for j in range(1, rep2 + 1):
            update(pos, M)
            in_val = bin(pos).count('1')
            for k in range(32):
                s = pos + (1 << k)
                if bin(s).count('1') <= in_val:
                    in_val = bin(s).count('1')
                    pos = s
                    if pos > MaxN:
                        break
                    update(pos, M)
            pos -= MaxN
        pos = back + plus
        if pos > MaxN:
            pos -= MaxN

if __name__ == "__main__":
    Q = int(input())
    queries = []
    for _ in range(Q):
        query = input().split()
        queries.append(query)

    for i in range(Q):
        if queries[i][0] == 'U':
            _, pos, M, plus = queries[i]
            pos, M, plus = map(int, [pos, M, plus])
            Update(pos, M, plus)
        else:
            _, pos1, pos2 = queries[i]
            pos1, pos2 = map(int, [pos1, pos2])
            print(read(pos2) - read(pos1 - 1))
