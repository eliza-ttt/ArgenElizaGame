import pygame
from pygame.locals import *

pygame.init()
# Высота и ширина
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')


# Запуск кода
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

