# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product
from string import ascii_lowercase, printable

m = int(input())
d = input().split()

for k in product(ascii_lowercase, repeat=3):
    valid_combination = True
    for i in range(m):
        xor_result = chr(int(d[i]) ^ ord(k[i % len(k)]))
        if xor_result not in " ();:,.'?-" + printable[:63]:
            valid_combination = False
            break
    if valid_combination:
        print("".join(k))
        break
