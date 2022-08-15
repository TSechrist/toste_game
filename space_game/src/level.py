import pygame

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visable_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):

        # update and draw the game
        pass