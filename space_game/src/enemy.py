import pygame
from settings import *
from entity import Entity
from utils import *

class Enemy(Entity):
	def __init__(self, enemy_name, pos, groups):
		
		# General Setup
		super().__init__(groups)
		self.sprite_type = 'enemy'
		
		# Graphics Setup
		self.import_graphics(enemy_name)
		self.status = 'idle'
		self.image = pygame.Surface((32, 32))
		self.rect = self.image.get_rect(topleft = pos)
		
	def import_graphics(self, name):
		self.animations = {'idle':[], 'move':[], 'attack':[]}
		main_path = f'../res/graphics/enemies/{name}/'
		for animation in self.animations.keys():
			self.animations[animation] = import_folder(main_path + animation)