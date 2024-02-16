from random import randint

from quorum.validation import equals


def try_max(equals, notequals, N, L, K, R):
    equals_f = sorted([(k, v) for k, v in equals.items()], key=lambda x: len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if len(equals[As]) > 0 and len(notequals[As]) < N * (K - 1) // (K) + R:
            return As
    return None


def try_question(equals, notequals, N, L, K, R):
    loops = N * 5
    while loops > 0:
        loops -= 1
        As = try_max(equals, notequals, N, L, K, R)
        if As is None:
            As = randint(1, N * (K - 1) // K) - 1
        Bs = randint(1, N) - 1
        if Bs == As:
            continue
        if len(notequals[As]) >= N * (K - 1) // K + R:
            continue
        if len(notequals[Bs]) >= N * (K - 1) // K + R:
            continue
        if As in equals[Bs] or Bs in equals[As]:
            continue
        if As in notequals[Bs] or Bs in notequals[As]:
            continue
        return (As, Bs)
    return None


def try_guess(equals_s, notequals, N, L, K):
    equals_f = [(k, v) for k, v in equals_s.items() if len(v) >= N // K + L]
    if len(equals_f) > 0:
        return equals_f[0][0]
    else:
        return None


def do_guess(equals_s, notequals, N, L, K, R):
    equals_f = sorted([(k, v) for k, v in equals_s.items()], key=lambda x: len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if len(equals[As]) > 0 and len(notequals[As]) < N * (K - 1) // (K) + R:
            return As
    return None


def next_question(N, pl_flag, L, K, L_max, queries):
    equals, notequals = {k: set() for k in range(N)}, {k: set() for k in range(N)}
    for q in queries:
        A, B, response = q
        A, B = int(A), int(B)
        if response == 'YES':
            equals[A].add(B)
            equals[B].add(A)
        else:
            notequals[A].add(B)
            notequals[B].add(A)

    min_guesses = (L + 1) * N / 2
    max_guesses = min_guesses * 5

    tg = try_guess(equals, notequals, N, L, K)
    if tg is not None:
        return tg

    done = False
    R = 0
    while not done:
        if len(queries) < max_guesses:
            tq = try_question(equals, notequals, N, L, K, R)
        else:
            tq = None
        if tq is not None:
            return tq
        tg = do_guess(equals, notequals, N, L, K, R)
        if tg is not None:
            return tg
        R += 1


# Read input
N, pl_flag, L, K, L_max = map(int, input().split())
D = int(input())
queries = [input().split() for _ in range(D)]

# Output
result = next_question(N, pl_flag, L, K, L_max, queries)
if isinstance(result, tuple):
    print(*result)
else:
    print(result)
