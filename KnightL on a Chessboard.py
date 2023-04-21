import sys

n = int(input().strip())


def allmoves(i, j, a, b, n):
    moves = []
    deltas = [(a, b), (a, -b), (-a, b), (-a, -b)]
    deltas.extend([(b, a), (b, -a), (-b, a), (-b, -a)])
    for delta in deltas:
        if i + delta[0] >= 0 and i + delta[0] < n and j + delta[1] >= 0 and j + delta[1] < n:
            moves.append((i + delta[0], j + delta[1]))
    return moves


def finddist(n, a, b):
    dist = [[-1 for x in range(n)] for x in range(n)]
    dist[n - 1][n - 1] = 0
    todo = [(n - 1, n - 1)]
    while len(todo) > 0:
        (i, j) = todo.pop(0)
        newmoves = allmoves(i, j, a, b, n)
        for move in newmoves:
            if dist[move[0]][move[1]] == -1:
                dist[move[0]][move[1]] = dist[i][j] + 1
                todo.append((move[0], move[1]))
                if move[0] == 0 and move[1] == 0:
                    break
    return dist[0][0]


ans = [[0 for x in range(n - 1)] for x in range(n - 1)]
for i in range(n - 1):
    for j in range(n - 1):
        ans[i][j] = finddist(n, i + 1, j + 1)
for i in range(n - 1):
    print(' '.join(map(str, ans[i])))