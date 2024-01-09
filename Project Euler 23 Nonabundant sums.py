# Enter your code here. Read input from STDIN. Print output to STDOUT

N = 100000
sumCache = [0] * (N + 1)

def isSumOfTwoAbundantNumbers(n):
    result = "NO"
    for i in range(12, n - 11):
        j = n - i
        if isAbundant(i) and isAbundant(j):
            return "YES"
    return result

def isAbundant(num):
    return getDivisorsSum(num) > num

def getDivisorsSum(n):
    if n == 0 or n == 1:
        return 0

    if sumCache[n] > 0:
        return sumCache[n]

    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i

    sumCache[n] = sum_divisors
    return sum_divisors

trials = int(input())

for _ in range(trials):
    num = int(input())
    result = isSumOfTwoAbundantNumbers(num)
    print(result)
