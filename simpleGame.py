import pygame,sys,random
from pygame.locals import *

pygame.init()
FPS=30
fpsClock=pygame.time.Clock()

DISPLAYSURF=pygame.display.set_mode((720,720))
pygame.display.set_caption('Fun Block')

blockImage = pygame.image.load('smallObject.png')


#randomRectangle = pygame.Rect(10,20,200,300)
pos = {"x":10,"y":10}
deltaX = 0
deltaY = 0
directionStart = 'right'

rate = 10
'''MAIN GAME LOOP'''
while True:
    DISPLAYSURF.fill((0,0,0))

    
    for event in pygame.event.get():
        
        deltaX = 0
        deltaY = 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deltaX = -(rate)
            if event.key == pygame.K_RIGHT:
                deltaX = rate
                print "Moving Left one block!"
            if event.key == pygame.K_UP:
                deltaY = -rate
            if event.key == pygame.K_DOWN:
                deltaY = (rate)       
        

            pos["x"] = pos["x"] + deltaX
            pos["y"] = pos["y"] + deltaY
        DISPLAYSURF.fill((0,0,0))
        DISPLAYSURF.blit(blockImage,(pos["x"],pos["y"]))
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS)
