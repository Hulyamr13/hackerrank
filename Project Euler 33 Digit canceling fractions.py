# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

def list_adder(strings, number):
    l = len(strings[0]) + 1
    lis = [string[:i] + str(number) + string[i:] for string in strings for i in range(l)]
    return lis

def permuter(lis1, lis2):
    while lis1:
        n = lis1.pop()
        lis2 = list_adder(lis2, n)
    return set(lis2)

def lis_to_str(list1):
    return ''.join([str(no) for no in list1])

def lis_to_int(list1):
    return int(''.join([str(no) for no in list1]))

item = input().split()
n = int(item[0])
k = int(item[1])

li1 = list(itertools.combinations_with_replacement(range(1, 10), r=k))
li2 = list(itertools.product(range(10), repeat=n - k))
li2.remove((0,) * (n - k))

answers = set()
li3 = []

for i in li1:
    li4 = []
    for j in li2:
        li4 += [(lis_to_int(j), int(i)) for i in permuter(list(i), [lis_to_str(j)]) if i[0] != '0']

    li3.append(li4)

for i in li3:
    for item in itertools.combinations(i, r=2):
        if item[0][0] < item[1][0] and item[0][0] * item[1][1] == item[1][0] * item[0][1]:
            answers.add((item[0][1], item[1][1]))

print(sum([a[0] for a in answers]), sum([a[1] for a in answers]))