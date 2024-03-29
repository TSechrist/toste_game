# Game Settings
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 32

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../res/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# General Colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#444444'
TEXT_COLOR = '#EEEEEE'

# UI Colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# Weapons
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15, 'graphic':'../res/graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30, 'graphic':'../res/graphics/weapons/lance/full.png'},
	'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'../res/graphics/weapons/rapier/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../res/graphics/weapons/axe/full.png'}
}

# Equipment
equipment_data = {
	'flame': {'strength': 5, 'cost': 20, 'graphic': '../res/graphics/particles/flame/fire.png'},
	'heal': {'strength': 20, 'cost': 10, 'graphic': '../res/graphics/particles/heal/heal.png'}
}

# Enemy Data
enemy_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../res/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 180},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../res/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 200},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../res/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 175},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../res/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 150}
}
# enemy_data = {
# 	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../res/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
# 	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../res/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
# 	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../res/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
# 	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../res/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
# }