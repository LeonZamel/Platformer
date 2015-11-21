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

        start_button.check_click()

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(start_button.render(), start_button.pos)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


class Button(object):
    def __init__(self, pos, size, color):
        self.size = size
        self.clicks = None
        self.color_u = color
        self.color_a = (222, 222, 0)
        self.color = self.color_u
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.color_a
            self.image.fill(self.color)
            if pygame.mouse.get_pressed()[0]:
                main.main()
        else:
            self.color = self.color_u
            self.image.fill(self.color)


    def render(self):
        return self.image

if __name__ == "__main__":
    menu()
