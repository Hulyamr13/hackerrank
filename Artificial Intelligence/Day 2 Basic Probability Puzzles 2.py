from fractions import Fraction


def func(count):
    for i in range(1, 7, 1):
        for j in range(1, 7, 1):
            if (i != j) and (i + j) == 6:
                count += 1

    return Fraction(count, 6 * 6)


print(func(0))