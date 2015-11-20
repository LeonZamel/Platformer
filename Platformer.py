import pygame
from pygame.locals import *
import sys
import main

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


def menu():
    start_button = Button((100, 50), (100, 100), GREEN)
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

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(start_button.render(), start_button.pos)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


class Button(object):
    def __init__(self, pos, size, color):
        self.pos = pos
        self.rect = pygame.Rect(pos, size)
        self.image = pygame.Surface(size)
        self.image.fill(color)

    def render(self):
        return self.image

if __name__ == "__main__":
    menu()
