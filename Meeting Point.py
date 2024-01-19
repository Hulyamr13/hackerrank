class Tuple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sum_x = 0
        self.sum_y = 0


def smartsolve(points):
    sum_val = 0
    n = len(points)

    points.sort(key=lambda p: p.x)

    for i in range(1, n):
        sum_val += abs(points[i].x - points[0].x)

    points[0].sum_x = sum_val

    for i in range(1, n):
        delta = abs(points[i].x - points[i - 1].x)
        points[i].sum_x = points[i - 1].sum_x + delta * i - delta * (n - i)

    sum_val = 0
    points.sort(key=lambda p: p.y)

    for i in range(1, n):
        sum_val += abs(points[i].y - points[0].y)

    points[0].sum_y = sum_val

    for i in range(1, n):
        delta = abs(points[i].y - points[i - 1].y)
        points[i].sum_y = points[i - 1].sum_y + delta * i - delta * (n - i)

    result = points[0].sum_x + points[0].sum_y

    for i in range(n):
        temp = points[i].sum_x + points[i].sum_y
        if temp < result:
            result = temp

    return result // 2


if __name__ == "__main__":
    n = int(input())
    points = []

    for _ in range(n):
        tempx, tempy = map(int, input().split())
        points.append(Tuple(tempx + tempy, tempy - tempx))

    print(smartsolve(points))
