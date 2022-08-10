import pygame
import os
from gameObject import gameObject

WIDTH, HEIGHT = 800, 600
ICON_WIDTH, ICON_HEIGHT = 50, 50
VEL = 5
BULLET_VEL = 10

CHEST_HIT = pygame.USEREVENT + 1

border = pygame.Rect(0, 0, WIDTH, HEIGHT)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Toste_engine")

WHITE = (255, 255, 255)
GREY = (100, 100, 100)

FPS = 60

PLAYER_1_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'player_1.png')), (ICON_WIDTH, ICON_HEIGHT))
CHEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'chest.png')), (ICON_WIDTH, ICON_HEIGHT))

def handle_bullets(bullets, player, chest):
    for bullet in bullets:
        bullet.x += BULLET_VEL
        if chest.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CHEST_HIT))
            bullets.remove(bullet)

def player_handle_movement(keys_pressed, player):
    if(keys_pressed[pygame.K_w] and player.box.y > 0): #Up
        player.box.y -= VEL
    if(keys_pressed[pygame.K_s] and player.box.y + player.box.height < border.height): #Down
        player.box.y += VEL
    if(keys_pressed[pygame.K_a] and player.box.x > 0): #Left
        player.box.x -= VEL
    if(keys_pressed[pygame.K_d] and player.box.x + player.box.width < border.width): #Right
        player.box.x += VEL
        

def draw_window(objlist):
    WIN.fill(GREY)
    for obj in objlist:
        WIN.blit(obj.image, (obj.box.x, obj.box.y))
    # WIN.blit(PLAYER_1_IMAGE, (player.x, player.y))
    # WIN.blit(CHEST_IMAGE, (chest.x, chest.y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    bullets = []

    # player = pygame.Rect(300, 100, ICON_WIDTH, ICON_HEIGHT)
    # chest = pygame.Rect(600, 400, ICON_WIDTH, ICON_HEIGHT)
    player = gameObject(PLAYER_1_IMAGE, pygame.Rect(300, 100, ICON_WIDTH, ICON_HEIGHT))
    chest = gameObject(CHEST_IMAGE, pygame.Rect(600, 400, ICON_WIDTH, ICON_HEIGHT))
    objlist = [player, chest]

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if(keys_pressed[pygame.K_e]): #E Key
                    bullets.append(pygame.Rect(player.x + player.width, player.y + (player.height/2), 10, 5))

        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)
        handle_bullets(bullets, player, chest)
        draw_window(objlist)
    
    pygame.quit()



if __name__ == "__main__":
    main()