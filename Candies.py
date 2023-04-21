def comp(p1, p2):
    return p1['rating'] - p2['rating']

N = int(input())
student = []
candies = [0] * N
ratings = []

for i in range(N):
    rating = int(input())
    student.append({'id': i, 'rating': rating})
    ratings.append(rating)

student.sort(key=lambda x: x['rating'])

sumcandies = 0

for i in range(N):
    id = student[i]['id']
    candy = 1

    if id > 0:
        if candies[id - 1] != 0 and ratings[id] > ratings[id - 1]:
            candy = candies[id - 1] + 1

    if id < N - 1:
        if candies[id + 1] != 0 and ratings[id] > ratings[id + 1] and candy <= candies[id + 1]:
            candy = candies[id + 1] + 1

    sumcandies += candy
    candies[id] = candy

print(sumcandies)
