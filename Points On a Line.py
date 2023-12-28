#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    points = []

    for _ in range(n):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        points.append((x, y))

    is_horizontal = all(point[1] == points[0][1] for point in points)
    is_vertical = all(point[0] == points[0][0] for point in points)

    if is_horizontal or is_vertical:
        print("YES")
    else:
        print("NO")
