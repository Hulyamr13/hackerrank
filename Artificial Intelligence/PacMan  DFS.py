from typing import List

class Node:
    def __init__(self, r: int, c: int, parent: 'Node' = None) -> None:
        self.r = r
        self.c = c
        self.parent = parent

def dfs(r: int, c: int, pacman_r: int, pacman_c: int, food_r: int, food_c: int, grid: List[str]) -> None:
    stack = []
    path = []
    explored = []
    visited = [[False] * c for _ in range(r)]
    goal = None

    init = Node(pacman_r, pacman_c, None)
    stack.append(init)

    while stack:
        curr = stack.pop()
        visited[curr.r][curr.c] = True
        explored.append(curr)

        if grid[curr.r][curr.c] == '.':
            goal = curr
            break

        if curr.r-1 >= 0 and not visited[curr.r-1][curr.c] and grid[curr.r-1][curr.c] != '%':
            newNode = Node(curr.r-1, curr.c, curr)
            visited[curr.r-1][curr.c] = True
            stack.append(newNode)
        if curr.c-1 >= 0 and not visited[curr.r][curr.c-1] and grid[curr.r][curr.c-1] != '%':
            newNode = Node(curr.r, curr.c-1, curr)
            visited[curr.r][curr.c-1] = True
            stack.append(newNode)
        if curr.c+1 < c and not visited[curr.r][curr.c+1] and grid[curr.r][curr.c+1] != '%':
            newNode = Node(curr.r, curr.c+1, curr)
            visited[curr.r][curr.c+1] = True
            stack.append(newNode)
        if curr.r+1 < r and not visited[curr.r+1][curr.c] and grid[curr.r+1][curr.c] != '%':
            newNode = Node(curr.r+1, curr.c, curr)
            visited[curr.r+1][curr.c] = True
            stack.append(newNode)

    curr = goal
    while curr:
        path.append(curr)
        curr = curr.parent

    print(len(explored))
    for node in explored:
        print(f"{node.r} {node.c}")
    print(len(path) - 1)
    while path:
        curr = path.pop()
        print(f"{curr.r} {curr.c}")

if __name__ == '__main__':
    pacman_r, pacman_c = map(int, input().split())
    food_r, food_c = map(int, input().split())
    r, c = map(int, input().split())
    grid = [input().strip() for _ in range(r)]
    dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)