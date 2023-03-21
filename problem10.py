s = input()
sorted_s = sorted(s, key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c))
print(''.join(sorted_s))
