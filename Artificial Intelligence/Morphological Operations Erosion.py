a = [[0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

s = [[1,1,1],
     [1,1,1],
     [1,1,1]]

def erosion(a, s):
    nrows, ncols = len(a), len(a[0])
    nrows_s, ncols_s = len(s), len(s[0])
    eroded = [[0] * ncols for i in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            if a[i][j] == 0:
                continue
            flag = True
            for k in range(nrows_s):
                for l in range(ncols_s):
                    ii, jj = i + k - 1, j + l - 1
                    if 0 <= ii < nrows and 0 <= jj < ncols:
                        if s[k][l] == 1 and a[ii][jj] == 0:
                            flag = False
                            break
                if not flag:
                    break
            if flag:
                eroded[i][j] = 1
    return eroded

eroded = erosion(a, s)
unique, freq = [], []
for i in range(len(eroded)):
    for j in range(len(eroded[0])):
        if eroded[i][j] == 1:
            unique.append(eroded[i][j])
freq = [unique.count(x) for x in unique]
print(freq[0])
