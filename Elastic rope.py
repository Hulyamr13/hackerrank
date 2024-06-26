# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from collections import deque

def points_equal(p1, p2):
    if p1[0] != p2[0] or p1[1] != p2[1]:
        return False
    return True

def orientation(points):
    if area_x2(points) > 0:
        return 'ccw'
    elif area_x2(points) < 0:
        return 'cw'
    else:
        return 'none'

def area_x2(points):
    area = 0
    n = len(points)
    for i in range(n):
        area += points[i][0] * (points[(i + 1) % n][1] - points[i - 1][1])
    return area

def point_in_triangle(point, triangle):
    if point in triangle:
        return False
    total_area = abs(area_x2(triangle))
    area1 = abs(area_x2([point, triangle[0], triangle[1]]))
    if area1 == 0:
        return False
    area2 = abs(area_x2([point, triangle[1], triangle[2]]))
    if area2 == 0:
        return False
    area3 = abs(area_x2([point, triangle[2], triangle[0]]))
    if area3 == 0:
        return False
    return total_area == (area1 + area2 + area3)

def slope(p1, p2):
    if p1[0] == p2[0]:
        return math.inf
    return (p1[1] - p2[1]) / (p1[0] - p2[0])

def graham_sort(points):
    points.sort()
    points = [points[0]] + sorted(points[1:], key=lambda point: slope(points[0], point))
    return points

def graham_scan(points):
    hull = []
    sorted_points = graham_sort(list(points)[:])
    for p in sorted_points:
        while len(hull) > 1 and orientation([hull[-2], hull[-1], p]) == 'cw':
            hull.pop()
        hull.append(p)
    return hull

def unwind(point, points_found, required_orientations, all_points):
    triangle = [points_found[-2], point, points_found[-1]]
    del points_found[-1]
    del required_orientations[-1]
    obstacle_points = []
    for p in all_points:
        if point_in_triangle(p, triangle):
            obstacle_points.append(p)
    if not obstacle_points:
        return
    obstacle_points.append(triangle[0])
    obstacle_points.append(triangle[1])
    obstacle_points_hull = deque(graham_scan(obstacle_points))
    for i, p in enumerate(obstacle_points_hull):
        if points_equal(p, triangle[0]):
            obstacle_points_hull.rotate(-i)
            break
    if len(points_found) > 1:
        triangle2 = [points_found[-2], points_found[-1], obstacle_points_hull[1]]
        while orientation(triangle2) != required_orientations[-1]:
            del points_found[-1]
            del required_orientations[-1]
            if len(points_found) <= 1:
                break
            triangle2 = [points_found[-2], points_found[-1], obstacle_points_hull[1]]
    for idx, p in enumerate(obstacle_points_hull):
        if idx != 0 and idx != len(obstacle_points_hull) - 1:
            points_found.append(p)
            required_orientations.append('ccw')

def add_point(point, points_found, required_orientations, all_points):
    if len(points_found) <= 1:
        points_found.append(point)
        required_orientations.append('cw')
        return
    triangle = [points_found[-2], points_found[-1], point]
    if orientation(triangle) == required_orientations[-1]:
        points_found.append(point)
        required_orientations.append('cw')
    else:
        unwind(point, points_found, required_orientations, all_points)
        add_point(point, points_found, required_orientations, all_points)

def compute_length(points):
    d = 0
    for i in range(len(points)-1):
        d += math.sqrt((points[i+1][0] - points[i][0])**2 + (points[i+1][1] - points[i][1])**2)
    return d

n, a, b = map(int, input().split())
a -= 1
b -= 1
points = [list(map(int, input().split())) for _ in range(n)]

if orientation(points) == 'ccw':
    cw_points = deque(reversed(points))
    a, b = n - (a + 1), n - (b + 1)
else:
    cw_points = deque(points[:])

x_a = cw_points[a]
x_b = cw_points[b]

max_length = -1

cw_points.rotate(-a)

for c in range(2):
    if c == 0:
        last_point = x_b
    else:
        last_point = x_a
    i = 0
    points_found = []
    required_orientations = []
    while points_equal(last_point, cw_points[i]) == False:
        add_point(cw_points[i], points_found, required_orientations, cw_points)
        i += 1
    add_point(last_point, points_found, required_orientations, cw_points)
    if c == 0:
        color = 'g'
    else:
        color = 'b'
    unique_points = [list(x) for x in set(tuple(x) for x in points_found)]
    if len(points_found) == len(unique_points):
        length = compute_length(points_found)
        if length > max_length:
            max_length = length
    cw_points.rotate(-i)

print(max_length)