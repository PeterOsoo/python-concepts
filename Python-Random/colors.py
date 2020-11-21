import random

colors = ['Red', 'Black', 'Green']

results = random.choices(colors, weights=[15, 15, 2], k=10)
print(results)
