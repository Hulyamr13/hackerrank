import math
import sys


def powSum(temp, N):
    result = 0

    for nmbr in temp:
        result += int(math.pow(nmbr, N))

    return result


def findAllDecompositions(X, N, upperBound, powSet, counter, result):
    # stopping condition
    if not powSet:
        result.append(counter)
        return

    newCounter = counter
    newPowSet = []

    for mmbr in powSet:
        indic = mmbr[-1]

        for nmbr in range(indic + 1, upperBound + 1):
            temp = []
            temp.extend(mmbr)
            temp.append(nmbr)

            tempSum = powSum(temp, N)

            if tempSum == X:
                # print(temp)
                newCounter += 1
            elif tempSum < X:
                newPowSet.append(temp)

    findAllDecompositions(X, N, upperBound, newPowSet, newCounter, result)


def numberOfAllDecompositions():
    inp = []

    for line in sys.stdin:
        inp.append(int(line))

    X = inp[0]
    N = inp[1]

    upperBound = math.floor(math.pow(X, 1 / N))
    powSet = []
    result = []

    # initialize the counter first
    if X == int(math.pow(upperBound, N)):
        counter = 1
    else:
        counter = 0

    for i in range(1, upperBound + 1):
        powSet.append([i])

    findAllDecompositions(X, N, upperBound, powSet, counter, result)

    print(result[0])


if __name__ == "__main__":
    numberOfAllDecompositions()