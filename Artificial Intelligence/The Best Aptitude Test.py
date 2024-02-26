# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        gpa = list(map(float, sys.stdin.readline().split()))
        gpamean = sum(gpa) / float(n)
        gpastdev = 0.0
        for j in range(n):
            gpastdev += (gpa[j] - gpamean) ** 2
        gpastdev = math.sqrt(gpastdev / float(n))
        bestind = -1
        maxcorr = 0
        for j in range(5):
            test = list(map(float, sys.stdin.readline().split()))
            testmean = sum(test) / float(n)
            teststdev = 0.0
            for k in range(n):
                teststdev += (test[k] - testmean) ** 2
            teststdev = math.sqrt(teststdev / float(n))
            tmpcorr = 0
            for k in range(n):
                tmpcorr += (test[k] - testmean) * (gpa[k] - gpamean)
            try:
                tmpcorr /= float(n) * teststdev * gpastdev
            except ZeroDivisionError:
                if abs(teststdev - gpastdev) < 1e-6:
                    tmpcorr = 1.0
                else:
                    tmpcorr = 0.0
            tmpcorr = abs(tmpcorr)
            if tmpcorr > maxcorr:
                maxcorr = tmpcorr
                bestind = j + 1
        print(bestind)

if __name__ == '__main__':
    main()
