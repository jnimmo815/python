import itertools, random

# make a deck of cards
deck = list(itertools.product(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],['C', 'D', 'H', 'S']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(1):
   print(deck[i][0], "of", deck[i][1])
