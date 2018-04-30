import pygame, random, sys
from pygame.locals import *

FPS=15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELLSIZE = 20

assert WINDOW_WIDTH % CELLSIZE ==0, "Window width must be a multiple of the size of the cells"

assert WINDOW_HEIGHT % CELLSIZE == 0, "Window Height must be a multiple of the size of the cells."

CELLWIDTH = int(WINDOW_WIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOW_HEIGHT/CELLSIZE)

# Red green and blue colors

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   =(255,0,0)
GREEN = (0,255,0)
DARKGREEN(0,155,0)
DARKGRAY=(40,40,40)
BGCOLOR=BLACK

UP='up'
DOWN='down'
LEFT='left'
RIGHT='right'

HEAD = 0

def main():
    global FPSCLOCK,DISPLAYSURF,BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clockl()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('Eating ass during CS 458')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame()
    #This is what makes a random start point for the snake
    startx = random.randint(5,CELLWIDTH-6)
    starty = random.randint(5,CELLHEIGHT-6)

    wormCoords = [{'x':startx, 'y':starty},
                    {'x':startx-1, 'y':starty},
                    {'x':start-2, 'y':starty}]

    direction = RIGHT

    apple = getRandomLocation()


    '''MAIN GAME LOOP'''
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if(event.key == K_LEFT or event.key == K_a) and direction !=RIGHT:
                    direction = LEFT
                if(event.key == K_RIGHT or event.key == K_d) and direction !=LEFT:
                    direction LEFT
                if(event.key == K_DOWN or event.key == K_s) and direction !=UP:
                    direction LEFT
                if(event.key == K_UP or event.key == K_w) and direction !=DOWN:
                    direction LEFT
                elif event.key == K_ESCAPE:
                    terminate()



        
                


