def solve(B):
    N = len(B)
    assert 1 <= N <= pow(10, 5)
    assert all(1 <= b <= 100 for b in B)

    llen, rlen = 0, 0
    right_pos = B[0]

    for i in range(1, N):
        new_llen = rlen + (right_pos - 1)
        new_right_pos = B[i]
        new_rlen = max(
            llen + (new_right_pos - 1),
            rlen + abs(new_right_pos - right_pos))

        llen, rlen = new_llen, new_rlen
        right_pos = new_right_pos

    return max(llen, rlen)


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        B = [int(X) for X in input().split()]
        print(solve(B))