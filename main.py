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

board_col = (165, 165, 162)
board_outline = (123, 123, 121)

cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60

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
                    block_col = block_middle
                elif block[1] == 1:
                    block_col = block_light
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2)
               
class board():

    def __init__(self):
       self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
    
    def moving(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1
    
    def draw(self):
        pygame.draw.rect(screen, board_col, self.rect)  
        pygame.draw.rect(screen, board_outline, self.rect, 2)
        
wall = wall()
wall.create_wall()
 
player_board = board()

#running
run = True
while run:
    
    clock.tick(fps)
    
    screen.fill(bg)
    wall.draw_wall()
    
    player_board.draw()
    player_board.moving()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()

