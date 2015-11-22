import Platformer
import Button
import main
import pygame
from pygame.locals import *
import sys


def start_menu():
    clicking = False
    start_button = Button.Button((Platformer.screen_center[0] - 500 / 2, 100), (500, 100),
                                 (Platformer.GREEN, Platformer.DARKGREEN), "Start game")
    levels_button = Button.Button((Platformer.screen_center[0] - 500 / 2, 300), (500, 100),
                                  (Platformer.GREEN, Platformer.DARKGREEN), "Levels")
    options_button = Button.Button((Platformer.screen_center[0] - 500 / 2, 500), (500, 100),
                                   (Platformer.GREEN, Platformer.DARKGREEN), "Options")
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
                clicking = True
            else:
                clicking = False

        if start_button.check_click(clicking):
            main.main("level1.map")
            break
        if levels_button.check_click(clicking):
            level_menu()
            break
        if options_button.check_click(clicking):
            options_menu()
            break

        Platformer.SCREEN.fill((255, 255, 255))
        Platformer.SCREEN.blit(start_button.render(), start_button.pos)
        Platformer.SCREEN.blit(levels_button.render(), levels_button.pos)
        Platformer.SCREEN.blit(options_button.render(), options_button.pos)
        pygame.display.flip()
        Platformer.FPSCLOCK.tick(Platformer.FPS)


def options_menu():
    clicking = False
    back_button = Button.Button((Platformer.screen_center[1] - 500 / 2, 300), (500, 100),
                                (Platformer.GREEN, Platformer.DARKGREEN), "Back")
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
                clicking = True
            else:
                clicking = False

        if back_button.check_click(clicking):
            start_menu()
            break

        Platformer.SCREEN.fill((255, 255, 255))
        Platformer.SCREEN.blit(back_button.render(), back_button.pos)
        pygame.display.flip()
        Platformer.FPSCLOCK.tick(Platformer.FPS)


def level_menu():
    clicking = False
    level_1_button = Button.Button((100, 100), (100, 100), (Platformer.GREEN, Platformer.DARKGREEN), "Level 1")

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
                clicking = True
            else:
                clicking = False

        if level_1_button.check_click(clicking):
            main.main("level1.map")
            break

        Platformer.SCREEN.fill((255, 255, 255))
        Platformer.SCREEN.blit(level_1_button.render(), level_1_button.pos)
        pygame.display.flip()
        Platformer.FPSCLOCK.tick(Platformer.FPS)
