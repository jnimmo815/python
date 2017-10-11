import sys
import pygame
from pygame.sprite import Group

from bridge_settings import Settings
from card import Card
from deal_test_5 import Deck



def run_game():
    #   Intialize game and create a screen object.
    pygame.init()   
    br_settings = Settings()
    deck = Deck()
    screen = pygame.display.set_mode(
        (br_settings.screen_width, br_settings.screen_height))
    pygame.display.set_caption("Bridge Bid Buddy")    
   
                
    hand_rank = []
    hand_suit = []    
  
    
    
    for i in range(13):
        hand_rank.append(deck.deck[i][0])
        hand_suit.append(deck.deck[i][1])
      
    print(deck.deck)   
    for i in range(13):
            print(hand_rank[i]  + hand_suit[i])  
        
    #   Start the main loop for the game.
    while True:
        
        #   Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                        
        
    
    #   Redraw the screen during each pass through the loop.
        screen.fill(br_settings.bg_color)        
              
        x_pos = br_settings.x_start_pos
        y_pos = br_settings.y_start_pos
        for i in range(13):
            x_pos = br_settings.x_start_pos +  i * 90
            rank = hand_rank[i]
            suit = hand_suit[i]
            #   Make a card.
            card = Card(rank, suit, screen)            
            card.blitme(x_pos, y_pos)         
                
                       
        # Make the recent draw screen visible.
        pygame.display.flip()      

run_game()
