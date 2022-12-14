import pygame, sys
from settings import *
from level import Level
from pytmx.util_pygame import load_pygame

class Game():
	def __init__(self):

		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Space Game")
		self.clock = pygame.time.Clock()
		tmx_data = load_pygame('../res/tiled/tmx/island1.tmx')
		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)



if __name__ == "__main__":
	game = Game()
	game.run()
