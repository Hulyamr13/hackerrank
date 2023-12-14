from heapq import heapify, heappush, heappop

def get_number_mixes(cookies, minimum_value):
    cookies = list(cookies)
    heapify(cookies)
    count = 0
    while cookies[0] < minimum_value:
        if len(cookies) < 2:
            return -1
        heappush(cookies, heappop(cookies) + 2 * heappop(cookies))
        count += 1
    return count

N, K = map(int, input().split())
A = map(int, input().split())
print(get_number_mixes(A, K))