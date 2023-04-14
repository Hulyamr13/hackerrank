a = [    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

s = [    [1,1,1],
    [1,1,1],
    [1,1,1]
]

nrows = len(a)
ncols = len(a[0])
se_rows = len(s)
se_cols = len(s[0])
origin_row = se_rows // 2
origin_col = se_cols // 2

dilated = [[0] * ncols for _ in range(nrows)]

for i in range(nrows):
    for j in range(ncols):
        if a[i][j]:
            for k in range(se_rows):
                for l in range(se_cols):
                    row = i - origin_row + k
                    col = j - origin_col + l
                    if (row >= 0 and row < nrows and col >= 0 and col < ncols):
                        dilated[row][col] = 1

count = 0
for row in dilated:
    count += sum(row)

print(count)