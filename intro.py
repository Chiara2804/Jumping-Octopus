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
tube_down = pygame.transform.flip(tube_up, False, True)
tube_middle = pygame.image.load('images/tile_0115.png')

#global costants
disp = pygame.display.set_mode((800, 800))
FPS = 50
VEL_ON = 3

#drawing elements
def draw():
    disp.blit(bg, (0,0))
    disp.blit(char, (char_x, char_y))
    disp.blit(ground, (ground_x, 700))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def initialization():
    global char_x, char_y, char_vel, ground_x
    char_x, char_y = 100, 50
    char_vel = 0
    ground_x = 0

initialization()

# Main
while True:
    ground_x -= VEL_ON
    if ground_x < 50: ground_x = 0

    char_vel += 1
    char_y = char_vel

    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                char_x -= 5
            if event.key == pygame.K_RIGHT:
                char_x += 5
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    draw()
    update()

