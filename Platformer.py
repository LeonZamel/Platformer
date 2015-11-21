import pygame
from pygame.locals import *
import sys
import Button


pygame.init()
# VARIABLES
screen = (1024, 1024)
# STATICS
SCREEN = pygame.display.set_mode(screen, DOUBLEBUF)
pygame.display.set_caption("Platformer")
FPS = 120
FPSCLOCK = pygame.time.Clock()
TILESIZE = 16
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
screen_center = (screen[0] / 2, screen[1] / 2)


def menu():
    start_button = Button.Button((screen_center[0] - 500 / 2, 100), (500, 100), GREEN, "Start game")
    options_button = Button.Button((screen_center[1] - 500 / 2, 300), (500, 100), GREEN, "Options")
    while True:
        # CHECK QUIT
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        start_button.check_click()
        options_button.check_click()

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(start_button.render(), start_button.pos)
        SCREEN.blit(options_button.render(), options_button.pos)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    menu()
