from re import T
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
ground = pygame.transform.scale(ground, (1600, 50))
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
font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

#
class Tube:
    def __init__(self):
        self.x = 300
        #self.y = random.randint(-75, 150)
        self.y = 150

    def go_on_and_draw(self):
        self.x -= VEL_ON
        disp.blit(tube_down, (self.x, self.y+210))
        disp.blit(tube_up, (self.x+80, self.y+500))

    def collision (self, char, char_x, char_y):
        toll = 2
        char__dx = char_x + char.get_width() - toll
        char__sx = char_x + toll
        tubes__dx = self.x
        tubes__sx = self.x + tube_down.get_width()
        char__up = char_y + toll
        char__down = char_y + char.get_height() - toll
        tubes__up = self.y + 110
        tubes__down = self.y + 210

        if char__dx > tubes__dx and char__sx < tubes__sx:
            if char__up < tubes__up and char__down > tubes__down:
                game_over()

    def between_tubes(self, char, char_x):
        toll = 2
        char__dx = char_x + char.get_width() - toll
        char__sx = char_x + toll
        tubes__dx = self.x
        tubes__sx = self.x + tube_down.get_width()
        if char__dx > tubes__dx and char__sx < tubes__sx:
            return True

# drawing elements
def draw():
    disp.blit(bg, (0,0))

    for t in tubes:
        t.go_on_and_draw()
    disp.blit(char, (char_x, char_y))
    disp.blit(ground, (ground_x, 700))
    points_render = font.render(str(points), 1, (255, 255, 255))
    disp.blit(points_render, (400, 0))

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def initialization():
    global char_x, char_y, char_vel
    global ground_x
    global tubes
    global points
    global between_tubes
    char_x, char_y = 200, 650
    char_vel = 0
    ground_x = 0
    points = 0
    tubes = []
    tubes.append(Tube())
    between_tubes = False

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
    if ground_x < -375: ground_x = 0
    ground_x -= VEL_ON

    # Commands
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                char_x -= 5
            if event.key == pygame.K_RIGHT:
                char_x += 5
            if event.key == pygame.K_DOWN:
                char_y += 10
            if event.key == pygame.K_UP:
                char_y -= 10

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if tubes[-1].x < 150: tubes.append(Tube())
    for t in tubes:
        t.collision(char, char_x, char_y)

    if not between_tubes:
        for t in tubes:
            if t.between_tubes(char, char_x):
                between_tubes = True
                break
    if between_tubes:
        between_tubes = False
        for t in tubes:
            if t.between_tubes(char, char_x):
                between_tubes = True
                break
        if not between_tubes:
            points += 1

    if char_y > 650:
        game_over()

    draw()
    update()
