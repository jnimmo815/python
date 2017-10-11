from random import shuffle

class Card(object):
    
    SUITS = ('C',  'D',  'H',  'S')
    RANKS = ('2',  '3',  '4',  '5',  '6',  '7',
             '8',  '9',  '10',  'J',  'Q', 'K', 'A')


    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.RANKS[self.rank],
                                   Card.SUITS[self.suit])
                                   
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range():
                self.cards.append(Card(rank, suit))
                




    

