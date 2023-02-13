import pygame
from settings import *
from utils import import_folder
from entity import Entity

class Player(Entity):
	def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_equipment):
		super().__init__(groups)
		# self.image = pygame.transform.scale(pygame.image.load('../res/test/player_1.png').convert_alpha(), (32, 32))
		self.image = pygame.transform.scale_by(pygame.image.load('../res/graphics/player/down/down_0.png').convert_alpha(), 2)
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0, -16)

		# graphics setup
		self.import_player_assets()
		self.status = 'down'

		# Movement
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None

		self.obstacle_sprites = obstacle_sprites

		# Weapon
		self.create_attack = create_attack
		self.destroy_attack = destroy_attack
		self.weapon_index = 0
		self.weapon = list(weapon_data.keys())[self.weapon_index]
		self.can_switch_weapon = True
		self.weapon_switch_time = None
		self.switch_duration_cooldown = 200

		# Equipment
		self.create_equipment = create_equipment
		self.equipment_index = 0
		self.equipment = list(equipment_data.keys())[self.equipment_index]
		self.can_switch_equipment = True
		self.equipment_switch_time = None

		# Stats
		self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'tech': 4, 'speed': 5}
		self.health = self.stats['health'] * 0.8
		self.energy = self.stats['energy'] * 0.4
		self.exp = 123
		self.speed = self.stats['speed']

	def import_player_assets(self):
		character_path = '../res/graphics/player/'
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)
		
	def input(self):
		keys = pygame.key.get_pressed()

		if not self.attacking:
			# Movement input
			if (keys[pygame.K_w] or keys[pygame.K_UP]) and not (keys[pygame.K_s] or keys[pygame.K_DOWN]):
				self.direction.y = -1
				self.status = 'up'
			elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not (keys[pygame.K_w] or keys[pygame.K_UP]):
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
				self.direction.x = -1
				self.status = 'left'
			elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not (keys[pygame.K_a] or keys[pygame.K_LEFT]):
				self.direction.x = 1
				self.status = 'right'
			else:
				self.direction.x = 0

			# Attack Input
			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()

			# Equipment Input
			if keys[pygame.K_LCTRL]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				style = list(equipment_data.keys())[self.equipment_index]
				strength = list(equipment_data.values())[self.equipment_index]['strength'] + self.stats['tech']
				cost = list(equipment_data.values())[self.equipment_index]['cost']
				self.create_equipment(style, strength, cost)

			# Weapon Switching
			if keys[pygame.K_q] and self.can_switch_weapon:
				self.can_switch_weapon = False
				self.weapon_switch_time = pygame.time.get_ticks()
				if self.weapon_index + 1 < len(list(weapon_data.keys())):
					self.weapon_index += 1
				else:
					self.weapon_index = 0
				self.weapon = list(weapon_data.keys())[self.weapon_index]
				
			# Equipment Switching
			if keys[pygame.K_e] and self.can_switch_equipment:
				self.can_switch_equipment = False
				self.equipment_switch_time = pygame.time.get_ticks()
				if self.equipment_index + 1 < len(list(equipment_data.keys())):
					self.equipment_index += 1
				else:
					self.equipment_index = 0
				self.equipment = list(equipment_data.keys())[self.equipment_index]

	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		# attack status
		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle', '_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack', '')

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
				self.destroy_attack()

		if not self.can_switch_weapon:
			if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
				self.can_switch_weapon = True

		if not self.can_switch_equipment:
			if current_time - self.equipment_switch_time >= self.switch_duration_cooldown:
				self.can_switch_equipment = True

	def animate(self):
		animation = self.animations[self.status]

		# loop over the frame index
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = pygame.transform.scale_by(animation[int(self.frame_index)].convert_alpha(), 2)
		self.rect = self.image.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)
