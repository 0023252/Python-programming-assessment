import pygame
import sys
from game_settings import *


#specifications
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
pygame.init()


#Character items
#player = Animation()



#Map sprites
Top_floor = pygame.image.load("Third_floor.png")
Middle_Floor = pygame.image.load("2nd_Floor.png")
Bottom_floor = pygame.image.load("1st_Floor.png")
Tutorial_map = pygame.image.load("Tutorial.png")





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









