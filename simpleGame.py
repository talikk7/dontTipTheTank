import pygame,sys,random, threading,time
from pygame.locals import *
from random import randint


''' GLOBAL VARIABLES '''

pygame.init()
FPS=30
fpsClock=pygame.time.Clock()

windowSize = 700 #this should be a square window

DISPLAYSURF=pygame.display.set_mode((windowSize,windowSize))
pygame.display.set_caption("Don't tip the tank!")

mainFish = pygame.image.load('static/simpleFish.png')
waterImage = pygame.image.load('static/waterBlock.png')

#randomRectangle = pygame.Rect(10,20,200,300)
pos = {"x":10,"y":10}
deltaX = 0
deltaY = 0
directionStart = 'right'
rate = 20
waterPos = (windowSize/2,windowSize/2)
totalWaterBlocks=10

def randBlockPos():
    global waterPos
    for b in xrange(totalWaterBlocks):
        waterPos = (randint(0,windowSize),randint(0,windowSize))
        time.sleep(3)
    
t = threading.Thread(target=randBlockPos)
t.start()

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
        DISPLAYSURF.blit(mainFish,(pos["x"],pos["y"]))
        DISPLAYSURF.blit(waterImage,waterPos)
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS)
