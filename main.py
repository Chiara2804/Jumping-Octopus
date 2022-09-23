from time import sleep
import pygame
import random

pygame.init()

# loading of images
bg = pygame.image.load('images/sky.jpg')
bg = pygame.transform.scale(bg, (800, 800))
char = pygame.image.load('images/character.png')
char = pygame.transform.scale(char, (50, 50))
char = pygame.transform.flip(char, True, False)
ground = pygame.image.load('images/tile_0002.png')
ground = pygame.transform.scale(ground, (50, 50))
tube_up = pygame.image.load('images/tile_0095.png')
tube_up = pygame.transform.scale(tube_up, (50, 50))
tube_down = pygame.transform.flip(tube_up, False, True)
tube_middle = pygame.image.load('images/tile_0115.png')
gameover = pygame.image.load('images/gameover.jpg')
gameover = pygame.transform.scale(gameover, (800, 800))

# global costants
disp = pygame.display.set_mode((800, 800))
FPS = 50
VEL_ON = 3

#
class Tube:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)
    def go_on_and_draw(self):
        self.x -= VEL_ON
        disp.blit(tube_down, (self.x, self.y+210))
        disp.blit(tube_up, (self.x, self.y+550))

# drawing elements
def draw():
    disp.blit(bg, (0,0))
    for t in tubes:
        t.go_on_and_draw()
    disp.blit(char, (char_x, char_y))
    disp.blit(ground, (ground_x, 700))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def initialization():
    global char_x, char_y, char_vel
    global ground_x
    global tubes
    char_x, char_y = 100, 650
    char_vel = 0
    ground_x = 0
    tubes = []
    tubes.append(Tube())

def game_over():
    disp.blit(gameover, (0, 0))
    update()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and event.key == pygame.K_SPACE:
                initialization()
                restart = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

initialization()

# Main
while True:
    # ground
    if ground_x < -40: ground_x = 800
    ground_x -= VEL_ON

    char_vel += 1
    char_x = char_vel

    # Commands
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                char_x -= 5
            if event.key == pygame.K_RIGHT:
                char_x += 5
            if event.key == pygame.K_DOWN:
                char_y += 5
            if event.key == pygame.K_UP:
                char_y -= 20

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if char_y > 650:
        game_over()

    draw()
    update()