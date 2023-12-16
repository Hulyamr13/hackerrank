import heapq

def minWait(allOrders) :
    totalWaitTime = 0
    numOrders = len(allOrders)
    if numOrders == 0 :
        return 0
    pendingOrders = []
    currentTime = allOrders[0][0]
    loop = True
    while loop :
        while len(allOrders) != 0 and allOrders[0][0] <= currentTime :
            order = heapq.heappop(allOrders)
            heapq.heappush(pendingOrders, (order[1], order[0]))
        if len(pendingOrders) != 0 :
            minWaitOrder = heapq.heappop(pendingOrders)
            waitTime = currentTime - minWaitOrder[1] + minWaitOrder[0]
            totalWaitTime += waitTime
            currentTime += minWaitOrder[0]
        else :
            currentTime += 1
        if len(pendingOrders) == 0 and len(allOrders) == 0 :
            loop = False
    return totalWaitTime/numOrders

n = int(input())
allOrders = []
for i in range(n) :
    line = input().split()
    l, t = int(line[0]), int(line[1])
    heapq.heappush(allOrders, (l, t))
print (int(minWait(allOrders)))