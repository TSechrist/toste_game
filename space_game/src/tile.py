import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		if sprite_type == 'object_rock' or sprite_type == 'object_tree':
			self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - (self.image.get_height() % TILESIZE)))
			if sprite_type == 'object_rock':
				diff = min(self.rect.height, 32)
				self.hitbox = self.rect
			else:
				diff = min(self.rect.height, 69)
				self.hitbox = self.rect.inflate(-80, 0)
			self.hitbox = pygame.Rect.move(self.hitbox, 0, abs(diff - self.rect.height))
			self.hitbox.height = diff
		else:
			self.rect = self.image.get_rect(topleft = pos)
			self.hitbox = self.rect.inflate(0, -10)