import pygame
from pygame.locals import *

pygame.init()
#width & height
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

bg = (69, 69, 81)
block_aqua = (230, 190, 231)
block_ocean= (206, 100, 210)
block_bottom= (146, 32, 149)

#running
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

