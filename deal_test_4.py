from itertools import product 
import random
from random import shuffle

class Card:
    
    FACES = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

class Deck:

    def __init__(self, ranks, suits):
        ranks = range(2, 14)
        suits = ['C', 'D', 'H', 'S']

        self.deck = []
        for r in ranks:
            for s in suits:
                self.deck.append(Card(r, s))                
        #   shuffle(deck)
print(Deck(2,2))
