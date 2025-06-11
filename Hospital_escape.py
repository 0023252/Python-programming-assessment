import pygame
import sys
from game_settings import *


#screen size
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
pygame.init()



#Map sprites
Third_floor = pygame.image.load("Third_floor.png")
Second_Floor = pygame.image.load("2nd_Floor.png")





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
    screen.blit(Third_floor,(0,0))
   
          

    
    
    
    
    
    
    
    
    
    
    pygame.display.update() 











