# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    limit = 1000000

    # count different layouts for a number of tiles
    solutions = [0] * (limit + 1)

    # start with smallest outer ring
    for outer in range(3, limit + 1):
        total = 0
        # add as many inner rings as possible
        inner = outer
        while inner >= 3:
            # tiles needed to create one ring whose sides are "inner" tiles long
            ring = 4 * (inner - 1)

            # running out of tiles ?
            if total + ring > limit:
                break

            # add valid ring
            total += ring
            solutions[total] += 1

            # decrement inner by 2 for next iteration
            inner -= 2

        # no more inner rings possible, abort
        if total == 0:
            break

    # pre-process all possible answers
    result = [0] * (limit + 1)
    one2ten = 0
    for i in range(len(solutions)):
        s = solutions[i]
        if 1 <= s <= 10:
            one2ten += 1

        result[i] = one2ten

    # process test cases
    tests = int(input())
    for _ in range(tests):
        last = int(input())
        # simple lookup
        print(result[last])

if __name__ == "__main__":
    main()
