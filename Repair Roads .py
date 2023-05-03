import os
import sys

#
# Complete the repairRoads function below.
#
import collections
import queue


def solve():
    n = int(input().strip())

    graph = dict((i, []) for i in range(0, n))

    for j in range(n - 1):
        x, y = [int(p) for p in input().strip().split()]
        graph[x].append(y)
        graph[y].append(x)

    level = 1

    root = 0
    q = queue.Queue()
    q.put((root, level, None))
    seen = set([])

    levels = collections.defaultdict(set)
    tree = {}

    while not q.empty():
        item, level, parent = q.get()
        levels[level].add(item)
        seen.add(item)

        tree[item] = dict(id=item, parent=parent, level=level, children=set([]),
                          leaf=None)

        for child in graph[item]:
            if child not in seen:
                q.put((child, level + 1, item))
                seen.add(child)
                tree[item]['children'].add(child)

    clusters = 1
    has_items_in_cluster = False

    for level in sorted(levels.keys(), reverse=True):
        for item in levels[level]:
            tree_item = tree[item]
            if not tree_item['children']:  # leaf
                tree_item['leaf'] = True
            else:
                has_items_in_cluster = True

                branches = 0
                for child in tree_item['children']:
                    if not tree[child]['leaf']:
                        branches += 1

                # branches == 0 -> visit point and go up
                # branches == 1 -> visit downstream, point and go up
                # branches % 2 == 0 -> have (branches // 2) clusters
                # branches % 2 == 1 -> have  (branches // 2) clusters and go up
                if branches >= 2:
                    new_clusters = branches // 2

                    clusters += new_clusters

                    if branches % 2 == 0:
                        has_items_in_cluster = False
                        parent = tree_item['parent']
                        if parent is not None:
                            tree[parent]['children'].remove(item)

    if not has_items_in_cluster:
        clusters -= 1

    print(clusters)


t = int(input().strip())

for tt in range(t):
    solve()