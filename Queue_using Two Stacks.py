old, new = [], []
for _ in range(int(input())):
    val = list(map(int,input().split()))
    if val[0] == 1:
        new.append(val[1])
    elif val[0] == 2:
        if not old :
            while new : old.append(new.pop())
        old.pop()
    else:
        print(old[-1] if old else new[0])