import pygame
from pygame.sprite import Sprite

from bridge_settings import Settings

class Card:
    """Define a card by rank, suit and points."""
    
    def __init__(self, rank, suit, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.rank = rank
        self.suit =suit
                
        #   Load the card image and get its rect.
        self.image = pygame.image.load('images/' + rank + '_of_' + suit + '.bmp')
        self.rect =self.image.get_rect()
        
                
        #   Place a card at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
                     
        #   Store the card's exact position.
        self.x = float(self.rect.x)
        
    def blitme(self, x_pos, y_pos):
        """Draw the card at its current location."""
        settings = Settings()
        self.screen.blit(self.image, (x_pos, y_pos))
        
        
        
        
        
        
        
        
        
        
        
    
