from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item, price = input().rsplit(' ', 1)
    price = int(price)
    if item not in items:
        items[item] = price
    else:
        items[item] += price

for item, price in items.items():
    print(f'{item} {price}')
