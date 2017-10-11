import itertools, random

class Deck:
    """Store deck information."""
    def __init__(self):        
        self.deck = deck
        FACES = {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
       
        
deck = list(itertools.product(['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A'],['C', 'D', 'H', 'S']))

# shuffle the cards
random.shuffle(deck)  
