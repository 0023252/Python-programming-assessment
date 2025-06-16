import pygame
from Hospital_escape import *

#Map sprites
Top_Floor = pygame.image.load("Third_floor.png")
Middle_Floor = pygame.image.load("2nd_Floor.png")
Bottom_floor = pygame.image.load("1st_Floor.png")
Tutorial_map = pygame.image.load("Tutorial.png")




#sprites for animation
player_sprite = [pygame.image.load("Colored_character.png"),
                 pygame.image.load("Colored_character(1).png"),
                 pygame.image.load("Colored_character(2).png"),
                 pygame.image.load("Colored_character(3).png"),
                 pygame.image.load("Colored_character(4).png"),
                 pygame.image.load("Colored_character(3).png"),
                 pygame.image.load("Colored_character(2).png"),
                 pygame.image.load("Colored_character(1).png")]

zombie_doctor = [pygame.image.load("Colored_doctor_zombie.png"),
                 pygame.image.load("Colored_doctor_zombie(1).png"),
                 pygame.image.load("Colored_doctor_zombie(2).png"),
                 pygame.image.load("Colored_doctor_zombie(3).png"),
                 pygame.image.load("Colored_doctor_zombie(2).png"),
                 pygame.image.load("Colored_doctor_zombie(1).png"),]

Hazmat_zombie = [pygame.image.load("Hazmat_suit_zombie_colored.png"),
                 pygame.image.load("Hazmat_suit_zombie_colored(1).png"),
                 pygame.image.load("Hazmat_suit_zombie_colored(2).png"),
                 pygame.image.load("Hazmat_suit_zombie_colored(3).png"),
                 pygame.image.load("Hazmat_suit_zombie_colored(2).png"),
                 pygame.image.load("Hazmat_suit_zombie_colored(1).png"),]

Patient_zombie = [pygame.image.load("zombie_patient_colored.png"),
                  pygame.image.load("zombie_patient_colored.(1)png"),
                  pygame.image.load("zombie_patient_colored(2).png"),
                  pygame.image.load("zombie_patient_colored(3).png"),
                  pygame.image.load("zombie_patient_colored(4).png"),
                  pygame.image.load("zombie_patient_colored(5).png"),
                  pygame.image.load("zombie_patient_colored(4).png"),
                  pygame.image.load("zombie_patient_colored(3).png"),
                  pygame.image.load("zombie_patient_colored(2).png"),
                  pygame.image.load("zombie_patient_colored(1).png")]