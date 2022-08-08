import pygame
import os

WIDTH, HEIGHT = 800, 600
ICON_WIDTH, ICON_HEIGHT = 50, 50
VEL = 5

border = pygame.Rect(0, 0, WIDTH, HEIGHT)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Toste_engine")

WHITE = (255, 255, 255)
GREY = (100, 100, 100)

FPS = 60

PLAYER_1_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'player_1.png')), (ICON_WIDTH, ICON_HEIGHT))
CHEST_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('../res', 'chest.png')), (ICON_WIDTH, ICON_HEIGHT))



def player_handle_movement(keys_pressed, player):
    if(keys_pressed[pygame.K_w] and player.y > 0): #Up
        player.y -= VEL
    if(keys_pressed[pygame.K_s] and player.y + player.height < border.height): #Down
        player.y += VEL
    if(keys_pressed[pygame.K_a] and player.x > 0): #Left
        player.x -= VEL
    if(keys_pressed[pygame.K_d] and player.x + player.width < border.width): #Right
        player.x += VEL

def draw_window(player, chest):
    WIN.fill(GREY)
    WIN.blit(PLAYER_1_IMAGE, (player.x, player.y))
    WIN.blit(CHEST_IMAGE, (chest.x, chest.y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    player = pygame.Rect(300, 100, ICON_WIDTH, ICON_HEIGHT)
    chest = pygame.Rect(600, 400, ICON_WIDTH, ICON_HEIGHT)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)
        draw_window(player, chest)
    
    pygame.quit()



if __name__ == "__main__":
    main()