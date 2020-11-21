sample import random

deck = list(range(1, 66))

hand = random.sample(deck, k=6)
print(hand)
