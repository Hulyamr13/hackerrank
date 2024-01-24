# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def iscurious_no(no):
    if sum([math.factorial(int(a)) for a in str(no)]) % no == 0:
        return True
    else:
        return False


n = int(input())
req_sum = 0

for i in range(10, n):
    if iscurious_no(i):
        req_sum += i

print(req_sum)
