n = int(input())
for i in range(n):
    line = input().rstrip()  # remove trailing whitespace
    line = line.replace(" && ", " and ")  # add spaces and replace '&&'
    line = line.replace(" || ", " or ")  # add spaces and replace '||'
    print(line)
