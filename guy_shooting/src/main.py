import pygame
import os
import random
from gameObject import gameObject

pygame.font.init()

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

SCORE_FONT = pygame.font.SysFont('ariel', 30)

PLAYER_1_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'player_1.png')), (ICON_WIDTH, ICON_HEIGHT))
CHEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'chest.png')), (ICON_WIDTH, ICON_HEIGHT))

def handle_bullets(bullets, player, chest):
    for bullet in bullets:
        bullet.x += BULLET_VEL
        if chest.box.colliderect(bullet):
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
        

def draw_window(objlist, bullets, score):
    WIN.fill(GREY)
    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (5, 5))
    for obj in objlist:
        WIN.blit(obj.image, (obj.box.x, obj.box.y))
    for bullet in bullets:
        pygame.draw.rect(WIN, WHITE, bullet)
    # WIN.blit(PLAYER_1_IMAGE, (player.x, player.y))
    # WIN.blit(CHEST_IMAGE, (chest.x, chest.y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    score = 0
    bullets = []

    # player = pygame.Rect(300, 100, ICON_WIDTH, ICON_HEIGHT)
    # chest = pygame.Rect(600, 400, ICON_WIDTH, ICON_HEIGHT)
    player = gameObject(PLAYER_1_IMAGE, pygame.Rect(300, 100, ICON_WIDTH, ICON_HEIGHT))
    chest = gameObject(CHEST_IMAGE, pygame.Rect(random.randint(50, 550), random.randint(0, 350), ICON_WIDTH, ICON_HEIGHT))
    objlist = [player, chest]

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # print(bullets)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e: #E Key
                    bullets.append(pygame.Rect(player.box.x + player.box.width, player.box.y + (player.box.height/2), 10, 5))
            if event.type == CHEST_HIT:
                objlist.remove(chest)
                chest = gameObject(CHEST_IMAGE, pygame.Rect(random.randint(50, 550), random.randint(0, 350), ICON_WIDTH, ICON_HEIGHT))
                objlist.append(chest)
                score += 1


        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)
        handle_bullets(bullets, player, chest)
        draw_window(objlist, bullets, score)
    
    pygame.quit()



if __name__ == "__main__":
    main()