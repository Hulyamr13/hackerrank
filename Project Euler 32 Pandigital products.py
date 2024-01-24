from itertools import permutations

# read highest digit
max_digit = int(input())

# all digits from 1..9
digits = list(range(1, 10))
# remove higher numbers so there is only 1..n left
digits = digits[:max_digit]

# all pandigital products
valid = set()

# create all permutations
for perm in permutations(digits):
    # let's say a * b = c
    # each variable contains at least one digit
    # the sum of their digits is limited by n (which should be 9)
    # try all combinations of lengths with the current permutation of digits
    for len_a in range(1, max_digit):
        for len_b in range(1, max_digit - len_a):
            len_c = max_digit - len_a - len_b

            # a*b=c => c>=a && c>=b => c has at least as many digits as a or b
            if len_c < len_a or len_c < len_b:
                break

            # build "a" out of the first digits
            a = int(''.join(map(str, perm[:len_a])))

            # next digits represent "b"
            b = int(''.join(map(str, perm[len_a:len_a+len_b])))

            # and the same for "c"
            c = int(''.join(map(str, perm[len_a+len_b:])))

            # is a*b = c ?
            if a * b == c:
                valid.add(c)

# find sum
result = sum(valid)
print(result)
