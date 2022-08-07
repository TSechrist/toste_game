import pygame
import os

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Toste_engine")

WHITE = (255, 255, 255)
GREY = (100, 100, 100)

FPS = 60

PLAYER_1_IMAGE = pygame.image.load(os.path.join('../res', 'player_1.png'))

def draw_window():
    WIN.fill(GREY)
    WIN.blit(PLAYER_1_IMAGE, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    
    pygame.quit()



if __name__ == "__main__":
    main()