import sys


def parse_input():
    n, m = input().strip().split(' ')
    n = int(n)
    m = int(m)
    A = [int(x) for x in input().strip().split(' ')]
    B = [int(x) for x in input().strip().split(' ')]
    return n, m, A, B


def initialize_table(n, m):
    table = dict()
    for i in range(0, n+1):
        loc = tuple([i, 0])
        table[loc] = list()

    for j in range(0, m+1):
        loc = tuple([0, j])
        table[loc] = list()
    return table


def populate_table(n, m, A, B, table):
    for i in range(1, n+1):
        for j in range(1, m+1):
            a = A[i-1]
            b = B[j-1]
            if a == b:
                seq = table[tuple([i-1, j-1])].copy()
                seq.append(a)
                table[tuple([i, j])] = seq
            else:
                ti = table[tuple([i-1, j])].copy()
                tj = table[tuple([i, j-1])].copy()

                if len(ti) > len(tj):
                    table[tuple([i, j])] = ti.copy()
                else:
                    table[tuple([i, j])] = tj.copy()
    return table


def output_result(out):
    out = ' '.join(str(x) for x in out)
    print(out)


def main():
    n, m, A, B = parse_input()
    table = initialize_table(n, m)
    table = populate_table(n, m, A, B, table)
    out = table[tuple([n, m])]
    output_result(out)


if __name__ == "__main__":
    main()
