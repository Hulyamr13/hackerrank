import pandas as pd
import numpy as np

n = int(input())
colnames = list(input().strip().split())

l1 = []
l2 = []
for i in range(0, n):
    x = list(input().strip().split())
    l1.append(x[2])
    l2.append(x[3])

ll1 = [np.nan if 'Missing' in i else float(i) for i in l1]
ll2 = [np.nan if 'Missing' in i else float(i) for i in l2]

int1 = pd.Series(ll1).interpolate(method='cubic', order=2)
int2 = pd.Series(ll2).interpolate(method='cubic', order=2)

res_data = []
for item, value in zip(l1, int1):
    if 'Missing' in item:
        res_data.append({'item': item, 'value': value})

for item, value in zip(l2, int2):
    if 'Missing' in item:
        res_data.append({'item': item, 'value': value})

res = pd.DataFrame(res_data)
res1 = pd.DataFrame({'index': [int(item.split('_')[1]) for item in res['item']], 'value': res['value']})
res1 = res1.sort_values(by=['index'])
x = res1.value.tolist()

for i in range(0, len(x)):
    print("%.2f" % x[i])
