import pygame 
import sys
from game_settings import *


#specifications
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
pygame.init()


#levels
main_menu = True 
tutorial = False
level_1 = False
level_2 = False
level_3 = False


#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False 
    
    #test/try
    screen.blit(Top_floor,(0,0))
   
          

    
    
    
    
    
    
    
    
    
    
    pygame.display.update()
    clock.tick(60) 









