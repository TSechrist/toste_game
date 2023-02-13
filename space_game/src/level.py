import pygame
from settings import *
from tile import Tile
from player import Player
from utils import *
from debug import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy


class Level:
	def __init__(self):

		# get the display surface
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# Attack Sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# User Interface
		self.UI = UI()

	def create_map(self):
		layouts = {
				'boundary': import_csv_layout('../res/tiled/tmx/island1_FloorBlocks.csv'),
				'bushes': import_csv_layout('../res/tiled/tmx/island1_Bushes.csv'),
				'objects': import_csv_layout('../res/tiled/tmx/island1_Objects.csv'),
				'entities': import_csv_layout('../res/tiled/tmx/island1_Entities.csv')
		}
		graphics = {
			'bushes': import_folder('../res/graphics/bushes'),
			'objects': import_folder_dict('../res/graphics/objects')
		}
		for style, layout in layouts.items():
			for row_index, row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x, y), [self.obstacle_sprites], 'invisible')
						if style == 'bushes':
							random_bush_image = choice(graphics['bushes'])
							Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_bush_image)
						if style == 'objects':
							surf = graphics['objects'][str(col)]
							if str(col) == "1":
								Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object_rock', surf)
							else:
								Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object_tree', surf)
						if style == 'entities':
							if str(col) == "15":
								#player
								self.player = Player(
									(x, y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_equipment)
							else:
								#enemy								
								if str(col) == "175": enemy_name = 'squid'
								elif str(col) == "176": enemy_name = 'raccoon'
								elif str(col) == "177": enemy_name = 'spirit'
								else: enemy_name = 'bamboo'
								
								Enemy(enemy_name, (x, y),
								[self.visible_sprites, self.attackable_sprites],
								self.obstacle_sprites)

	def create_attack(self):
		self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def create_equipment(self, style, strength, cost):
		print(style)
		print(strength)
		print(cost)

	def run(self):

		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.UI.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		#General Setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../res/graphics/maps/island1.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

	def custom_draw(self, player):

		# Getting offsets
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf, floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image, offset_pos)
			
	def enemy_update(self, player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)