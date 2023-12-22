# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

count = 0

for _ in range(N):
    tweet = input()
    if 'hackerrank' in tweet.lower():
        count += 1

print(count)