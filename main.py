import pygame
from pygame.locals import *

pygame.init()
#width & height
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

bg = (69, 69, 81)
block_light = (230, 190, 231)
block_middle= (206, 100, 210)
block_bottom= (146, 32, 149)

cols = 6
rows = 6

class wall():

    def __init__(self):
        self.width = screen_width // cols
        self.height = 50
    
    def create_wall(self):
        self.blocks = []

        block_individual = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1

                block_individual = [rect, strength]
                block_row.append(block_individual)

            self.blocks.append(block_row)
       
    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                if block[1] == 3:
                    block_col = block_bottom
                elif block[1] == 2:
                    block_col = block_ocean
                elif block[1] == 1:
                    block_col = block_aqua
                pygame.draw.rect(screen, block_col, block[0])
                
wall = wall()
wall.create_wall()
      

#running
run = True
while run:
    
    screen.fill(bg)
    wall.draw_wall
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update(

pygame.quit()

