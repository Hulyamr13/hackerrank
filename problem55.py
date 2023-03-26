n, m = map(int, input().split())
arr = list(map(int, input().split()))
likes = set(map(int, input().split()))
dislikes = set(map(int, input().split()))

happiness = 0
for num in arr:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1

print(happiness)
