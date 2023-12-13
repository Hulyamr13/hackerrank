import heapq

def cuts_cost(y, x):
    heapq.heapify(y)
    heapq.heapify(x)

    hori_segs = 1
    vert_segs = 1
    total = 0
    while y and x:
        cost_y = heapq.heappop(y)
        cost_x = heapq.heappop(x)

        if (cost_y < cost_x) or (cost_y == cost_x and vert_segs <= hori_segs):
            heapq.heappush(x, cost_x)
            highest = cost_y
            total += hori_segs * highest
            vert_segs += 1
        else:
            heapq.heappush(y, cost_y)
            highest = cost_x
            total += vert_segs * highest
            hori_segs += 1

    total += hori_segs * sum(y)
    total += vert_segs * sum(x)

    return -total % (10**9 + 7)


num_tests = int(input().strip())
for test in range(num_tests):
    m, n = tuple(int(i) for i in input().strip().split(" "))
    costs_y = [-int(i) for i in input().strip().split(" ")]
    costs_x = [-int(i) for i in input().strip().split(" ")]
    print(cuts_cost(costs_y, costs_x))