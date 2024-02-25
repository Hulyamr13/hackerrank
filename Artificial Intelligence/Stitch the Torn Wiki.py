# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

#LOCAL = True
LOCAL = False

LA = []
LB = []

def process_text(s):
    l = s.split()
    d = {}
    totalw = 0
    for w in l:
        if w[0].isupper():
            if w in d:
                if d[w] >= 3:
                    continue
                d[w] += 1
            else:
                d[w] = 1
            totalw += 1
    return (d, totalw)

def read_data():
    global LA, LB

    if LOCAL:
        f = open("x.txt", "r")
    else:
        f = sys.stdin

    n = int(f.readline())

    for k in range(n):
        s = f.readline()
        LA.append(process_text(s))

    f.readline()

    for k in range(n):
        s = f.readline()
        LB.append(process_text(s))

bmatch = []

def match():
    global bmatch
    scores = []
    for i in range(len(LA)):
        da, ta = LA[i]
        for j in range(len(LB)):
            db, tb = LB[j]
            ncommon = 0
            for w in da:
                if w in db:
                    ncommon += min(da[w], db[w])
            cscore = float(ncommon) / (ta + tb - ncommon)
            scores.append((cscore, i, j))

    scores.sort()
    matcheda = {}
    matchedb = {}

    scores.reverse()
    #print scores

    for i in range(len(LA)):
        bmatch.append(-1)

    for score, i, j in scores:
        if (i not in matcheda) and (j not in matchedb):
            bmatch[i] = j
            matcheda[i] = 1
            matchedb[j] = 1

def write_output():
    global bmatch
    for i in bmatch:
        sys.stdout.write(str(i + 1) + "\n")

read_data()
match()
write_output()
