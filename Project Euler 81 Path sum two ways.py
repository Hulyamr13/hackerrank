def find_min_path_sum(grid):
    rows=len(grid)
    columns=len(grid)
    res=[[0]*len(grid) for i in range(len(grid))]
    res[0][0]=grid[0][0]
    for i in range(1,rows):
        res[i][0]=res[i-1][0]+grid[i][0]
    for j in range(1,columns):
        res[0][j]=res[0][j-1]+grid[0][j]
    for i in range(1,rows):
        for j in range(1,columns):
            res[i][j]=grid[i][j]+min(res[i-1][j],res[i][j-1])
    return res[rows-1][columns-1]
n=int(input().strip())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().strip().split())))
print(find_min_path_sum(grid))