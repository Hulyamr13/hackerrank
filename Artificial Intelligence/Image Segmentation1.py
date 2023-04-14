import numpy as np

def expandnode(grid, visited, noder2, nodec2, count):
    # create temp variables
    tempr = noder2
    tempc = nodec2

    # create stack and add current to it, row in first, then column, so col first out
    stack = [(tempr, tempc)]

    # change start node to visited
    visited[tempr][tempc] = True

    while stack:
        # pop last vector(column at end, then row)
        tempr, tempc = stack.pop()

        # push unvisited 4-neighbors equal to 1 to queue
        if tempr > 0 and grid[tempr-1][tempc] == 1 and not visited[tempr-1][tempc]:
            stack.append((tempr-1, tempc))
            visited[tempr-1][tempc] = True

        if tempr < 3 and grid[tempr+1][tempc] == 1 and not visited[tempr+1][tempc]:
            stack.append((tempr+1, tempc))
            visited[tempr+1][tempc] = True

        if tempc > 0 and grid[tempr][tempc-1] == 1 and not visited[tempr][tempc-1]:
            stack.append((tempr, tempc-1))
            visited[tempr][tempc-1] = True

        if tempc < 11 and grid[tempr][tempc+1] == 1 and not visited[tempr][tempc+1]:
            stack.append((tempr, tempc+1))
            visited[tempr][tempc+1] = True

    # this cycle will keep exploring stack in dfs/bfs first manner until all connected marked
    # as visited
    count += 1

    return count

if __name__ == '__main__':
    # mimic input matrix
    row0 = [0,0,0,1,1,0,0,0,1,0,1,0]
    row1 = [1,1,1,0,1,1,1,1,0,0,0,1]
    row2 = [1,1,1,0,1,0,0,1,0,0,1,0]
    row3 = [1,0,0,0,0,0,0,0,0,1,0,0]
    grid = np.array([row0, row1, row2, row3])

    # establish visited grid
    visited = np.zeros((4, 12), dtype=bool)

    # establish base count of objects(all connected groups of 1)
    count = 0

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == 1 and not visited[i][j]:
                count = expandnode(grid, visited, i, j, count)

    print(count)
