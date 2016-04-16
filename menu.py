import Platformer
import Button
import main
import pygame
from pygame.locals import *
import sys


class Start(object):
    def level1(self):
        main.c_level = "level1.map"
        main.main()


class Menu(object):
    def __init__(self):
        self.buttons = []
        self.funcs = []
        self.clicking = False

    def run(self):
        while True:
            # CHECK EVENTS
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONUP:
                    self.clicking = True
                else:
                    self.clicking = False

            for num, button in enumerate(self.buttons):
                if button.check_click(self.clicking):
                    self.clicking = False
                    button.func()
                    break

            Platformer.SCREEN.fill((255, 255, 255))
            for button in self.buttons:
                Platformer.SCREEN.blit(button.render(), button.pos)
            pygame.display.flip()
            Platformer.FPSCLOCK.tick(Platformer.FPS)

start = Start()
start_menu = Menu()
options_menu = Menu()
levels_menu = Menu()
# START MENU

start_button = Button.Button(start.level1, (Platformer.screen_center[0] - 500 / 2, 100), (500, 100),
                             (Platformer.GREEN, Platformer.DARKGREEN), "Start game")
levels_button = Button.Button(levels_menu.run, (Platformer.screen_center[0] - 500 / 2, 300), (500, 100),
                              (Platformer.GREEN, Platformer.DARKGREEN), "Levels")
options_button = Button.Button(options_menu.run, (Platformer.screen_center[0] - 500 / 2, 500), (500, 100),
                               (Platformer.GREEN, Platformer.DARKGREEN), "Options")

start_menu.buttons.extend((start_button, levels_button, options_button))

# OPTIONS MENU

back_button = Button.Button(start_menu.run, (Platformer.screen_center[1] - 500 / 2, 500), (500, 100),
                            (Platformer.GREEN, Platformer.DARKGREEN), "Back")
resolution_button = Button.Button(start_menu.run, (Platformer.screen_center[1] - 500 / 2, 100), (500, 100),
                                  (Platformer.GREEN, Platformer.DARKGREEN), "Change resolution")

options_menu.buttons.extend((back_button, resolution_button))

# LEVELS MENU

level_1_button = Button.Button(start.level1, (100, 100), (100, 100), (Platformer.GREEN, Platformer.DARKGREEN), "Level 1")
back_button = Button.Button(start_menu.run, (Platformer.screen_center[1] - 500 / 2, 300), (500, 100),
                            (Platformer.GREEN, Platformer.DARKGREEN), "Back")

levels_menu.buttons.extend((level_1_button, back_button))
