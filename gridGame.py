import sys, time
from threading import Thread
from random import randint
from pprint import pprint
import pygame

def checkCollision():
    global health
    global _EXIT

    while _EXIT is False:
        status = health.inc()
        print "inside checkCollision: ", health.printBuffer()
        if status is True:
            print "Health goes up!"
        
        time.sleep(randint(2,5))

    print "Exiting check Collision Thread"
    return 0

def decrimentHealth():
    global health
    global _EXIT

    while _EXIT is False:
        status = health.dec()
        print "inside decrimentHealth: ", health.printBuffer()
        if status is False:
            print "The fish is dead!"
            _EXIT = True

        time.sleep(randint(0,3))

    print "Exiting Decriment Health Thread"
    return 0

class semaphore(object):
    def __init__(self,name, initValue ):
        self._BUFFER_VAL = initValue
        self._START_VAL = initValue
        self._NAME = name

    def dec(self):
        if self._BUFFER_VAL < 0:
            return False
        else:
            self._BUFFER_VAL-=1
            return True

    def inc(self):
        if self._BUFFER_VAL == self._START_VAL:
            return False
        else:
            self._BUFFER_VAL+=1

    def printBuffer(self):
        print "Buffer: " + str(self._NAME) + ":" + str(self._BUFFER_VAL) + "/" + str(self._START_VAL)

    def returnBufferVal(self):
        return int(self._BUFFER_VAL)

class gameMachine(object):
    def __init__(self):
    #Global Variables
        pygame.init()
        pygame.font.init()
        self._FPS = 15
        self._FPS_CLOCK = pygame.time.Clock()
    #Game Engine Settings
        self._windowSize = 500
        self._numCells = 5
        self._DISPLAYSURF = pygame.display.set_mode((self._windowSize,self._windowSize))
        pygame.display.set_caption("Don't Tip the Tank!")
        self._FONT = pygame.font.SysFont('Comic Sans MS',30)
      #Character images
        self._MAINFISH = pygame.image.load('static/simpleFish.png')
        self._WATERBLOCK = pygame.image.load('static/waterBlock.png')
        
    #Grid Variables
        self.startDiameter = self._windowSize / self._numCells
        self.startPosition = [ self._windowSize/2 , self._windowSize - (self.startDiameter/2) ]
    #Color Codes
        self._OLIVE = (128,128,0)
        self._BLUE = (0,0,255)
        self._WHITE = (255,255,255)
        self._GREEN = (0,255,0)
        self._BLACK = (0,0,0)
    def constructGrid(self):

        tempFactor = self._numCells
        grid = []

        for i in xrange(0,self._numCells):
            row = []
            for j in xrange(0,self._numCells):
                row.append( [[i,j],tempFactor] )
            grid.append(row)
            tempFactor-=1

        

        pprint( grid )
                
               
    def drawFish(self,color,side,thickness):
        pygame.draw.circle(self._DISPLAYSURF,color,self.startPosition,side,thickness)

    def quitGame(self):
        pygame.quit()
        sys.exit()
    
    def getEvents(self):
        return pygame.event.get()
    
    def displayImages(self):    
        pygame.display.flip()

    def updateDisplay(self):
        pygame.display.update()

    def printGameTime(self):
        print self._FPS_CLOCK.get_time()

    def getScreen(self):
        return self._DISPLAYSURF 


''' GAME MAIN '''
_EXIT = False
g = gameMachine()
g.constructGrid()
health = semaphore("Health",10)

threads = []
threads.append( Thread(target=checkCollision))
threads.append( Thread(target=decrimentHealth))

for thing in threads:
    thing.start()

while _EXIT is False:
    g._DISPLAYSURF.fill(g._OLIVE)

    for event in g.getEvents():
        if event.type == pygame.QUIT:
            _EXIT = True
            g.quitGame()

    g._DISPLAYSURF.fill(g._OLIVE)
    _SCOREBOARD = g._FONT.render("Tank Status: " + str(health.returnBufferVal()), False, (0,0,0))

    g._DISPLAYSURF.blit(_SCOREBOARD,(0,0))
    g.drawFish(g._BLUE,90,0)
    g.displayImages()
    g.updateDisplay()
    g._FPS_CLOCK.tick(g._FPS)
