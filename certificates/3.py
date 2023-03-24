def numCells(grid):
    res = 0
    i = 0
    while i < len(grid):
        k = 0
        while k < len(grid[0]):
            val = grid[i][k]
            flag = 1
            ii = max(0, i - 1)
            while ii < min(len(grid), i + 2) and flag == 1:
                kk = max(0, k - 1)
                while kk < min(len(grid[0]), k + 2) and flag == 1:
                    if (ii, kk) != (i, k) and val <= grid[ii][kk]:
                        flag = 0
                        break
                    kk += 1
                ii += 1
            if flag == 1:
                res += 1
            k += 1
        i += 1
    return res

