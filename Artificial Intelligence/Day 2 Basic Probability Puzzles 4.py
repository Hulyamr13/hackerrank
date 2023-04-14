from fractions import Fraction

bag1 = ['r'] * 4 + ['b'] * 5
bag2 = ['r'] * 3 + ['b'] * 7

combo = []
visited = 0

for i in bag1:
    for e, j in enumerate(bag2):
        for k in bag2[e + 1:]:
            temp = [i, j, k]
            if (temp.count('r') == 1) and (temp.count('b') == 2):
                combo.append(temp)

            visited += 1

print(Fraction(len(combo), visited))