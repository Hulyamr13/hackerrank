import sys, math, re
from collections import deque

testing = [False]

def build_match_remover(subs):
    subs2 = []
    char_to_rep = {}
    for kw in subs:
        kw_chars = set(kw)
        if len(kw_chars) == 1:
            k = char_to_rep.get(kw[0])
            char_to_rep[kw[0]] = len(kw) if k is None else min(len(kw), k)
        else:
            subs2.append([kw, kw_chars, None])
    for c, k in char_to_rep.items():
        subs2.append([c * k, {c}, None])
    subs = subs2

    subs.sort(key=lambda x: len(x[0]), reverse=True)
    for sub in subs:
        clause = re.escape(sub[0])
        sub[2] = re.compile("(?=({}))".format(clause))

    def process(code):
        n = len(code)
        chars = set(code)
        exclude = [False] * n
        imin = 0
        for ipat, sub in enumerate(subs):
            if not (sub[1] <= chars):
                continue
            kw, pat = sub[0], sub[2]
            last_match_end = 0
            istart = max(0, imin - len(kw))
            for match in pat.finditer(code[istart:]):
                i1, i2 = max(last_match_end, match.start(1)), match.end(1)
                exclude[istart + i1:istart + i2] = [True] * (i2 - i1)
                last_match_end = i2 - 1
            while imin < n and exclude[imin]:
                imin += 1
            if imin == n:
                break

        return "".join([c for i, c in enumerate(code) if exclude[i] is False])

    return process

def remove_matches(process, srcs):
    return [process(s) for s in srcs]

def test_remove_matches():
    print("Testing remove_matches")
    for srcs, subs, eans in [
        [["11110111101111101110"], ["111", "11110"], ["0"]]
    ]:
        remover = build_match_remover(subs)
        ans = remove_matches(remover, srcs)
        if ans != eans:
            print("FAIL: {}: {}/{}: Expected {}, got {}".format("remove matches", srcs, subs, eans, ans))

def test_frobenius(frobenius):
    for a, eans in [
        [[3, 5], 7],
        [[6, 9, 20], 43],
        [[66488, 66613, 66643, 66669, 66670, 66673, 66768, 66782, 66806, 66860], 12168243]
    ]:
        ans = frobenius(a)
        if ans != eans:
            print("FAIL: {}: {}: Expected {}, got {}".format(frobenius.__name__, a, eans, ans))

def frobenius_dqqd(a):
    a.sort()
    k = len(a)
    a1 = a[0]
    n = [0] + [math.inf] * (a1 - 1)
    for i in range(1, k):
        d = math.gcd(a1, a[i])
        for r in range(0, d):
            nmin = min([n[q] for q in range(r, r + a1, d)])
            if nmin < math.inf:
                for _ in range(a1 // d):
                    nmin = nmin + a[i]
                    p = nmin % a1
                    nmin = min(nmin, n[p])
                    n[p] = nmin
    return max(n) - a1

def frobenius_bfd_updated(a):
    a.sort()
    n = len(a)
    a1 = a[0]
    Q, Qset = deque(), set()
    Q.append(0)
    Qset.add(0)
    P = [n - 1] * a1
    S = [0] + [a[0] * a[n - 1]] * (a1 - 1)
    Amod = [x % a1 for x in a]

    while Q:
        v = Q.popleft()
        Qset.remove(v)
        for j in range(1, P[v] + 1):
            u = v + Amod[j]
            if u >= a1:
                u -= a1
            w = S[v] + a[j]
            if w == S[u]:
                if j < P[u]:
                    P[u] = j
            elif w < S[u]:
                S[u] = w
                P[u] = j
                if u not in Qset:
                    Q.append(u)
                    Qset.add(u)
    return max(S) - a1

def frobenius_rr_updated(a):
    a.sort()
    k = len(a)
    a1 = a[0]
    n = [0] + [math.inf] * (a1 - 1)
    for i in range(1, k):
        d = math.gcd(a1, a[i])
        for r in range(0, d):
            nmin = min([n[q] for q in range(r, r + a1, d)])
            if nmin < math.inf:
                for _ in range(a1 // d):
                    nmin = nmin + a[i]
                    p = nmin % a1
                    nmin = min(nmin, n[p])
                    n[p] = nmin
    return max(n) - a1

def answer(codes, keywords):
    codes = set(codes)
    remover = build_match_remover(keywords)
    lens = []
    g = None
    for code in codes:
        code = remover(code)
        k = len(code)
        if k == 0:
            continue
        if k == 1:
            return 0
        g = math.gcd(g, k) if g is not None else k
        lens.append(k)
    if not lens or g != 1:
        return -1
    lens.sort()
    if testing[0]:
        print("Removed substrings", file=sys.stderr)
    return frobenius_dqqd(lens)

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--test":
        testing[0] = True
        for f in [frobenius_bfd_updated, frobenius_rr_updated]:
            print("Testing {}".format(f.__name__))
            test_frobenius(f)
        test_remove_matches()
    ncodes = int(sys.stdin.readline())
    codes = [sys.stdin.readline().strip() for _ in range(ncodes)]
    nkeywords = int(sys.stdin.readline())
    keywords = [sys.stdin.readline().strip() for _ in range(nkeywords)]
    if testing[0]:
        print("Read input", file=sys.stderr)
    print(answer(codes, keywords))

main()
