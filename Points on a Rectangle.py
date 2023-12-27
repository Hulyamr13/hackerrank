def lies_on_v(x, y, x1, y1, y2):
    if x != x1:
        return False
    if y < y1 or y > y2:
        return False
    return True

def validate(x1, x2, y1, y2, x, y):
    if x1 >= x2 or y1 >= y2:
        return False
    for i in range(len(x)):
        if (lies_on_v(x[i], y[i], x1, y1, y2) or lies_on_v(x[i], y[i], x2, y1, y2)
            or lies_on_v(y[i], x[i], y1, x1, x2) or lies_on_v(y[i], x[i], y2, x1, x2)):
            continue
        return False
    return True

tests = int(input())
for _ in range(tests):
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    xs = [-100000, 100000]
    ys = [-100000, 100000]
    for i in range(n):
        xs.append(x[i])
        ys.append(y[i])

    flag = 0
    for i in range(len(xs)):
        for j in range(len(xs)):
            for q in range(len(ys)):
                for w in range(len(ys)):
                    if validate(xs[i], xs[j], ys[q], ys[w], x, y):
                        flag = 1

    if flag == 0:
        print("NO")
    else:
        print("YES")
