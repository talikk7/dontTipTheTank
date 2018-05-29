import sys

class gameMachine(object):

	import pygame,random,threading,time
	from random import randint

	def __init__(self):
	#Global Variables
		self.pygame.init()
		self.pygame.font.init()
		self._FPS = 15
		self._FPS_CLOCK = self.pygame.time.Clock()


	#Game Engine Settings
		self._windowSize = 500
		self._DISPLAYSURF = self.pygame.display.set_mode((self._windowSize,self._windowSize))
		self.pygame.display.set_caption("Don't Tip the Tank!")
		self._FONT = self.pygame.font.SysFont('Comic Sans MS',30)

	#Game Mechanic Settings
		self._TANKFILL = 0
		self._TANKSCORE = self._FONT.render("Tank Status: " + str(self._TANKFILL), False, (0,0,0))

	#Character images
		self._MAINFISH = self.pygame.image.load('static/simpleFish.png')
		self._WATERBLOCK = self.pygame.image.load('static/waterBlock.png')

	#Color Codes
		self._OLIVE = (128,128,0)

	''' GAME FUNCTIONS '''

	def quitGame(self):
		self.pygame.quit()
		sys.exit()

g = gameMachine()
while True:
	g._DISPLAYSURF.fill(g._OLIVE)

	for event in g.pygame.event.get():
		if event.type == g.pygame.QUIT:
			g.quitGame()

	g._DISPLAYSURF.fill(g._OLIVE)
	g._DISPLAYSURF.blit(g._TANKSCORE,(0,0))
	g.pygame.display.flip()
	g.pygame.display.flip()
	g.pygame.display.update()
	g._FPS_CLOCK.tick(g._FPS)			
