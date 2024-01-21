def build_quadtree(pts):
    num = len(pts)
    yvals = sorted(pt[1] for pt in pts)
    box = (pts[0][0], yvals[0], pts[-1][0], yvals[-1])
    subtrees = []
    point_list = []

    if box[0] < box[2] or box[1] < box[3]:
        i = (len(pts) - 1) // 2
        x = pts[i][0]
        y = yvals[i]
        parts = [[], [], [], []]

        for pt in pts:
            i = 1 if pt[0] > x else 0
            if pt[1] > y:
                i += 2
            parts[i].append(pt)

        for subpts in parts:
            if len(subpts) > 8:
                subtrees.append(build_quadtree(subpts))
            else:
                point_list.extend(subpts)

    return {"num": num, "box": box, "subtrees": subtrees, "pts": point_list}


def count_points(node, boxes):
    for box in boxes:
        if (
            node["box"][0] >= box[0]
            and node["box"][1] >= box[1]
            and node["box"][2] <= box[2]
            and node["box"][3] <= box[3]
        ):
            return node["num"]

    keep = [box for box in boxes if node["box"][0] <= box[2] and node["box"][1] <= box[3] and node["box"][2] >= box[0] and node["box"][3] >= box[1]]

    n = 0

    if keep:
        for x, y in node["pts"]:
            for box in keep:
                if x >= box[0] and y >= box[1] and x <= box[2] and y <= box[3]:
                    n += 1
                    break

        for subtree in node["subtrees"]:
            n += count_points(subtree, keep)

    return n


def to_boxes(pts):
    edges = []
    q = pts[-1]

    for p in pts:
        if p[1] == q[1]:
            if p[0] < q[0]:
                edges.append((p[0], q[0], p[1]))
            else:
                edges.append((q[0], p[0], p[1]))
        q = p

    edges.sort()
    i = 0
    boxes = []
    active = []
    left = edges[i][0]

    while i < len(edges) and edges[i][0] <= left:
        active.append(edges[i])
        i += 1

    while active:
        right = min(edge[1] for edge in active)

        if i < len(edges) and edges[i][0] < right:
            right = edges[i][0]

        active.sort(key=lambda edge: edge[2])

        for j in range(0, len(active), 2):
            boxes.append((left, active[j][2], right, active[j + 1][2]))

        active = [edge for edge in active if edge[1] > right]

        while i < len(edges) and edges[i][0] <= right:
            active.append(edges[i])
            i += 1

        left = right

    return boxes


def read_pts(N):
    pts = []

    for _ in range(N):
        x, y = map(int, input().split())
        pts.append((x, y))

    return pts


N, Q = map(int, input().split())
points = read_pts(N)
points.sort()
quad_tree = build_quadtree(points)

for _ in range(Q):
    M = int(input())
    query_points = read_pts(M)
    query_boxes = to_boxes(query_points)
    print(count_points(quad_tree, query_boxes))
