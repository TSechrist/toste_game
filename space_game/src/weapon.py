import pygame

class Weapon(pygame.sprite.Sprite):
	def __init__(self, player, groups):
		super().__init__(groups)
		direction = player.status.split('_')[0]

		# Graphic
		full_path = f'../res/graphics/weapons/{player.weapon}/{direction}.png'
		self.image = pygame.transform.scale_by(pygame.image.load(full_path).convert_alpha(), 0.5)
		# self.image = pygame.Surface((20,20))
		
		# Placement
		if direction == 'up':
			self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-5, 0))
		elif direction == 'down':
			self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-5, 0))
		elif direction == 'left':
			self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0, 8))
		elif direction == 'right':
			self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0, 8))
