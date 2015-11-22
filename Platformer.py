import pygame
from pygame.locals import *
import menu


pygame.init()
# VARIABLES
screen = (1000, 800)
screen_center = (screen[0] / 2, screen[1] / 2)
SCREEN = pygame.display.set_mode(screen, DOUBLEBUF)
pygame.display.set_caption("Platformer")
FPS = 120
FPSCLOCK = pygame.time.Clock()

TILESIZE = 16
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)


if __name__ == "__main__":
    menu.start_menu.run()
