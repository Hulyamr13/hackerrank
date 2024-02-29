# Enter your code here. Read input from STDIN. Print output to STDOUT


n_inputs = int(input())

list_dates = []
list_prices = []
for row in range(n_inputs):
    raw_inp = input().split(sep=" ")
    list_dates.append(raw_inp[0]), list_prices.append(raw_inp[-1].split(sep="\t")[-1])

missing_indices = []
for i in range(len(list_prices)):
    try:
        list_prices[i] = float(list_prices[i])
    except:
        missing_indices.append(i)

predictions = []
for i in missing_indices:
    list_floats = []
    a,b = i-1, i+1
    while len(list_floats)<1:
        a, b = max(0, a-1), b+1
        for j in list_prices[a:b]:
            if type(j) == float:
                list_floats.append(j)


for i in range(20):
    print(-1e32)