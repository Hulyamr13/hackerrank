# Enter your code here. Read input from STDIN. Print output to STDOUT

def becomes89(x):
    while True:
        # sum of squares of all digits
        square_digit_sum = 0
        reduce = x
        while reduce > 0:
            digit = reduce % 10
            reduce //= 10
            square_digit_sum += digit * digit

        # terminated?
        if square_digit_sum == 89:
            return True
        if square_digit_sum == 1:
            return False

        # not done yet ... next iteration
        x = square_digit_sum


def main():
    digits = int(input())

    # Hackerrank's result will become quite big, they only want the final number modulo 1000000007
    # (doesn't affect the original problem)
    Modulo = 1000000007

    # count how many numbers with the same digit sum exist
    # inspired by https://rosettacode.org/wiki/Iterated_digits_squaring

    # initialized with zeros
    sums = [0] * (200 * 9 * 9 + 1)

    # single-digit numbers
    for first in range(10):
        sums[first * first] += 1

    # start with one digit and iteratively add digits
    for length in range(2, digits + 1):
        # go through all potential sums (including the most recently added digit)
        for sum_ in range(length * 9 * 9, 0, -1):
            # what sum is it without that most recently added digit?
            for high in range(1, 10):
                # square of the just added digit
                square = high * high
                # this digit can't be part of the current digit sum because it's too big
                if square > sum_:
                    break

                # add count of all numbers without the new digit
                sums[sum_] += sums[sum_ - square]
                # avoid overflows (Hackerrank only)
                sums[sum_] %= Modulo

    # now we know how many numbers sums[x] exist with digit sum x
    # let's check which digit sums will be converted to 89
    count89 = 0
    # check all sums
    for i in range(1, digits * 9 * 9 + 1):
        if becomes89(i):
            count89 += sums[i]  # yes, all these numbers turn to 89
            count89 %= Modulo  # Hackerrank only

    print(count89)


if __name__ == "__main__":
    main()
