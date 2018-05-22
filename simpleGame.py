import pygame,sys,random, threading,time
from pygame.locals import *
from random import randint


''' GLOBAL VARIABLES '''

pygame.init()
pygame.font.init()
FPS=15
fpsClock=pygame.time.Clock()



windowSize = 300 #this should be a square window
gridBlockSize = 10 #This is used to make a discrete grid for the game.
gridFactor = windowSize/gridBlockSize

DISPLAYSURF=pygame.display.set_mode((windowSize,windowSize)) #see how its a square window
pygame.display.set_caption("Don't tip the tank!")
theFont = pygame.font.SysFont('Comic Sans MS', 30)

#init the scoreboard
_SCORE = 0
scoreBoard = theFont.render("Score: " + str(_SCORE), False, (0,0,0))


#here are some random images
mainFish = pygame.image.load('static/simpleFish.png')
waterImage = pygame.image.load('static/waterBlock.png')
_OLIVE = (128,128,0)

#randomRectangle = pygame.Rect(10,20,200,300)
pos = {"x":10,"y":10}
deltaX = 0
deltaY = 0
directionStart = 'right'
rate = 10
waterPos = {"x":windowSize/2,"y":windowSize/2}
totalWaterBlocks=10
evaporation=3

''' FUNCTIONS FOR FUNCTIONALITY '''
def incrementScore():
    global theFont
    global scoreBoard
    global _SCORE
    _SCORE = _SCORE + 1
    scoreBoard = theFont.render("Score: " + str(_SCORE),False,(0,0,0))

#This should check if the waterBlock is within the fish block
def _compareTuple(t1,t2):
    if(t1["x"] == t2["x"]) and (t2["y"] == t2["y"]):
        return True
    else:
        return False

def checkCollision(thing1,thing2):
    if( _compareTuple(thing1,thing2) ):
        print "THERE IS A COLLISION"
        print "Thing 1:", thing1
        print "Thing 2:", thing2
        return True
    else:
        return False



''' THREADING THINGS '''
def randBlockPos():
    #Updates the water blocks position 
    global waterPos
    for b in xrange(totalWaterBlocks):
        tempRandX = randint(0,gridBlockSize) * gridFactor
        tempRandY = randint(0,gridBlockSize) * gridFactor
        waterPos = {"x":tempRandX,"y":tempRandY}
        time.sleep(evaporation)
    
t = threading.Thread(target=randBlockPos)
t.start()

'''MAIN GAME LOOP'''
while True:
    DISPLAYSURF.fill(_OLIVE)
    for event in pygame.event.get():
        
        #resets position changes
        deltaX = 0
        deltaY = 0
        
        #Keyboard Events
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deltaX = -(rate)
            if event.key == pygame.K_RIGHT:
                deltaX = rate

            if event.key == pygame.K_UP:
                deltaY = -rate
            if event.key == pygame.K_DOWN:
                deltaY = (rate)       
        
            #updates the position
            pos["x"] = pos["x"] + deltaX
            pos["y"] = pos["y"] + deltaY
        
        
        if checkCollision( waterPos,pos ):
            incrementScore() #magic number for the score

    #updates the screen
    DISPLAYSURF.fill(_OLIVE)
    DISPLAYSURF.blit(mainFish,(pos["x"],pos["y"]))
    DISPLAYSURF.blit(waterImage,(waterPos["x"],waterPos["y"]) )
    DISPLAYSURF.blit(scoreBoard,(0,0))
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)
