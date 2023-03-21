N = int(input())

for i in range(N):
    line = input()
    line = line.replace(' && ', ' and ').replace(' || ', ' or ')
    line = line.replace('&& ', 'and ').replace(' ||', ' or')
    print(line)
