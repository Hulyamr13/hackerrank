#!/bin/python3

import math
import os
import random
import re
import sys

primesq = 32000

isprime = [True] * primesq
primelist = []
isprime[0] = False
isprime[1] = False
for i in range(2, primesq):
    if isprime[i]:
        primelist.append(i)
        for j in range(i * i, primesq, i):
            isprime[j] = False


def theta(n):
    toret = 1
    for p in primelist:
        if p * p > n:
            break
        if n % p == 0:
            toret *= p - 1
            n //= p
            while n % p == 0:
                toret *= p
                n //= p
    if n == 1:
        return toret
    else:
        return toret * (n - 1)


def solveb1p(n, a, p):
    if a == 0:
        return (n + 1) % p
    if a % (p - 1) == 0:
        return (n - n // p) % p
    a = a % (p - 1)
    factlist = [1]
    for i in range(1, a + 2):
        factlist.append((factlist[-1] * i) % p)
    factinvlist = [1] * len(factlist)
    factinvlist[-1] = pow(factlist[-1], p - 2, p)
    for i in range(len(factinvlist) - 1, 0, -1):
        factinvlist[i - 1] = (factinvlist[i] * i) % p

    bernlist = [0] * (a + 1)
    bernlist[0] = 1
    for i in range(1, a + 1):
        for j in range(i):
            bernlist[i] -= bernlist[j] * factinvlist[i - j + 1]
        bernlist[i] = bernlist[i] % p
    bernlist[1] = p - bernlist[1]

    npow = pow(n, a + 1, p)
    ninv = pow(n, p - 2, p)
    toret = 0
    for i in range(a + 1):
        toret += bernlist[i] * npow * factinvlist[a + 1 - i]
        npow = (npow * ninv) % p
    return (toret * factlist[a]) % p


def solveb1(n, a, b, p, e):
    if e == 1:
        return solveb1p(n, a, p)
    bdiv = (b - 1) // p
    m = pow(p, e)
    thetam = (m * (p - 1)) // p

    choosetable = [[1] + [0] * (e - 1)]
    while (True):
        line = [1] + [0] * (e - 1)
        for i in range(1, e):
            line[i] = (choosetable[-1][i - 1] + choosetable[-1][i]) % (m // p)
        if len(choosetable) > n + 1 or line == choosetable[0]:
            break
        choosetable.append(line)

    toret = 0

    replen = m * len(choosetable) // math.gcd(m, len(choosetable))
    for j in range(e):
        mult = pow(p * bdiv, j, m)
        toadd = 0
        if n + 1 >= replen:
            repval = 0
            for i in range(replen):
                repval += pow(i, a, m) * choosetable[i % len(choosetable)][j]
            toadd = (((n + 1) // replen) * repval) % m
        for i in range((n + 1) % replen):
            toadd += pow(i, a, m) * choosetable[i % len(choosetable)][j]
        toret += mult * toadd
    return toret % m


def solvebnot1(n, a, b, m):
    thetam = theta(m)

    choosetable = [[1]]
    for i in range(1, a + 1):
        choosetable.append([0] * (i + 1))
        choosetable[i][0] = 1
        for j in range(1, i):
            choosetable[i][j] = (choosetable[i - 1][j - 1] + choosetable[i - 1][j]) % m
        choosetable[i][i] = 1

    bmininv = pow(b - 1, thetam - 1, m)
    outputvec = [0] * a + [1]
    toret = 0
    for i in range(a, -1, -1):
        pm = -1
        for j in range(i - 1, -1, -1):
            outputvec[j] += (pm * choosetable[i][j] * bmininv * outputvec[i]) % m
            pm = -pm
        toret += b * bmininv * outputvec[i] * pow(n, i, m) * pow(b, n, m)

    return (toret - outputvec[0] * bmininv * b + (1 if a == 0 else 0)) % m


def combine(x1, m1, theta1, x2, m2, theta2):
    a = m2 * pow(m2, theta1 - 1, m1)
    b = m1 * pow(m1, theta2 - 1, m2)
    return (a * x1 + b * x2) % (m1 * m2)


def solve(n, a, b, m):
    if a == 0:
        curr = n + 1
        toret = 0
        toadd = 1
        tomult = b
        while curr > 0:
            if curr % 2:
                toret = (toret * tomult + toadd) % m
            toadd = (toadd * tomult + toadd) % m
            tomult = (tomult * tomult) % m
            curr //= 2
        return toret
    currval = 0
    currmod = 1
    currtheta = 1
    for p in primelist:
        if (b - 1) % p == 0:
            nump = 0
            ppow = 1
            thetamult = p - 1
            while m % p == 0:
                m //= p
                nump += 1
                ppow *= p
                thetamult *= p
            if nump > 0:
                currval = combine(currval, currmod, currtheta, solveb1(n, a, b, p, nump), ppow, thetamult)
                currmod *= ppow
                currtheta *= thetamult

    p = math.gcd(b - 1, m)
    if p != 1:
        currval = combine(currval, currmod, currtheta, solveb1(n, a, b, p, 1), p, p - 1)
        currmod *= p
        currtheta *= p - 1
        m //= p
    return combine(currval, currmod, currtheta, solvebnot1(n, a, b, m), m, theta(m))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        m = int(first_multiple_input[3])

        result = solve(n, a, b, m)

        fptr.write(str(result) + '\n')

    fptr.close()