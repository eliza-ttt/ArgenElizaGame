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
block_middle = (206, 100, 210)
block_bottom = (146, 32, 149)

board_col = (250, 250, 250)
board_outline = (200, 200, 200)

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
        pygame.draw.rect(screen, board_outline, self.rect, 3)

class game_ball():
    def __init__(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x,self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0

    def moving(self):
        collision_thresh = 5

        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                if self.rect.colliderect(item[0]):
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                         self.speed_y *= -1
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_y > 0:
                        self.speed_x *= -1
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                         self.speed_x *= -1
                    if wall.blocks[row_count][item_count][1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)

                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0

                item_count += 1
            row_count += 1

        if wall_destroyed == 1:
            self.game_over

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        if self.rect.top < 0:
            self.speed_y *= -1

        if self.rect.bottom > screen_height:
            self.game_over = -1


        if self.rect.colliderect(player_board):
            if abs(self.rect.bottom - player_board.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_board.direction
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

    def draw(self):
        pygame.draw.circle(screen, board_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, board_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)


wall = wall()
wall.create_wall()

player_board = board()

ball = game_ball(player_board.x + (player_board.width // 2), player_board.y - player_board.height)

# running
run = True
while run:

    clock.tick(fps)

    screen.fill(bg)

    wall.draw_wall()

    player_board.draw()
    player_board.moving()

    ball.draw()
    ball.moving()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    pygame.display.update()

    pygame.display.update()

pygame.quit()
