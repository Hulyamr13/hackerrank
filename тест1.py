import random

played_combinations = [sorted(random.sample(range(1, 50), 6)) for i in range(10000)]
print(played_combinations)
