def name_score(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name_value = sum(alphabet.index(letter) + 1 for letter in name)
    return name_value

n = int(input())

names = [input().strip() for _ in range(n)]

sorted_names = sorted(names)

q = int(input())
for _ in range(q):
    query = input().strip()
    score = (sorted_names.index(query) + 1) * name_score(query)
    print(score)
