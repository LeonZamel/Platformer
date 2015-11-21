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
    start_button = Button((100, 50), (500, 100), GREEN, "Start game")
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
    def __init__(self, pos, size, color, text):
        self.font_family = pygame.font.get_default_font()
        self.font = pygame.font.Font(self.font_family, 20)
        self.text = text
        self.font_image = self.font.render(self.text, True, BLACK, )
        self.font_rect = self.font_image.get_rect()
        self.size = size
        self.center = (self.size[0] / 2 - self.font_rect.centerx, self.size[1] / 2 - self.font_rect.centery)
        self.clicks = None
        self.color_u = color
        self.color_a = (0, 220, 0)
        self.color = self.color_u
        self.pos = pos
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = self.color_a
            if pygame.mouse.get_pressed()[0]:
                main.main()
        else:
            self.color = self.color_u

    def render(self):
        self.image.fill(self.color)
        self.image.blit(self.font_image, self.center)
        return self.image

if __name__ == "__main__":
    menu()
