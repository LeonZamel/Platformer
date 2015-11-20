import pygame
from pygame.locals import *

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

if __name__ == "__main__":
    main.main()
