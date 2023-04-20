import copy

n, m, fin = map(int, input().split())
sec = 1

def printans(g):
    for val in g:
        print("".join(val))

g = []
save = []
timer = [[0 for x in range(m)] for y in range(n)]
for i in range(n):
    s = input()
    g.append(list(s))

save.append(copy.deepcopy(g))
save.append(copy.deepcopy(g))

for t in range(1, 5):
    sec = sec + 1
    for i in range(n):
        for j in range(m):
            if g[i][j] != 'O':
                g[i][j] = 'O'
                timer[i][j] = sec

    save.append(copy.deepcopy(g))

    dx = [+0, +0, +1, -1]
    dy = [+1, -1, +0, +0]
    g2 = copy.deepcopy(g)

    sec = sec + 1
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'O' and timer[i][j] == sec - 3:
                g2[i][j] = '.'
                for k in range(4):
                    di = i + dx[k]
                    dj = j + dy[k]
                    if di >= 0 and di < n and dj >= 0 and dj < m:
                        g2[di][dj] = '.'

    g = copy.deepcopy(g2)
    save.append(copy.deepcopy(g))

if fin == 1:
    printans(save[fin])
elif fin % 2 == 0:
    printans(save[2])
elif fin % 4 == 1:
    printans(save[5])
elif fin % 4 == 3:
    printans(save[3])