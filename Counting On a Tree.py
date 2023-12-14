import sys
from math import gcd
from collections import defaultdict

sys.setrecursionlimit(10**9)

def dfs1():
    '''keep 1 node as root and calculate how many arrows are pointing towards it'''
    root = 1
    seen = {root, }
    stack = [root]
    count = 0
    while stack:
        root = stack.pop()
        for node in tree[root]:
            if node not in seen:
                seen.add(node)
                count += (root, node) in guess    # if root is parent of node
                stack.append(node)
    return count

def dfs2(cost, k):
    '''now make every node as root and calculate how many nodes
       are pointed towards it; If u is the root node for which
       dfs1 calculated n (number of arrows pointed towards the root)
       then for v (adjacent node of u), it would be n-1 as v is the
       made the parent now in this step (only if there is a guess, if
       there is no guess then it would be not changed)'''
    root = 1
    seen = {root,}
    stack = [(root, cost)]
    t_win = 0
    while stack:
        (root, cost) = stack.pop()
        t_win += (cost >= k)
        for node in tree[root]:
            if node not in seen:
                seen.add(node)
                stack.append((node, cost - ((root, node) in guess) + ((node, root) in guess)))
    return t_win


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    tree = defaultdict(list)

    for a1 in range(n-1):
        u,v = map(int, input().strip().split(' '))
        tree[u].append(v)
        tree[v].append(u)

    g,k = map(int, input().strip().split(' '))
    guess = {tuple(map(int, input().split())) for _ in range(g)}

    cost = dfs1()
    win = dfs2(cost, k)
    g = gcd(win, n)
    print("{0}/{1}".format(win//g, n//g))