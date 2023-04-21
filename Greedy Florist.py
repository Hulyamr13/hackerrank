def getMinimumCost(k, c):
    c.sort(reverse=True) # Sort the array in descending order
    totalCost = 0 # Initialize total cost to 0

    for i in range(len(c)):
        totalCost += ((i // k) + 1) * c[i] # Calculate cost based on previous purchases

    return totalCost

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
