import Platformer
import configparser
import math
import pygame
from pygame.locals import *
import sys


def main():
    clicking = False
    level = Level("level1.map")
    level.build_map()
    player = Player()

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

        player.move()
        # Platformer.SCREEN
        Platformer.SCREEN.fill((255, 255, 255))
        Platformer.SCREEN.blit(level.render_map(), (0, 0))
        Platformer.SCREEN.blit(player.render(), (player.rect.x, player.rect.y))

        pygame.display.flip()
        Platformer.FPSCLOCK.tick(Platformer.FPS)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image_name = ""
        pygame.sprite.Sprite.__init__(self)
        self.keys_pressed = []
        self.y_vel = 0
        self.speed = 2
        self.width = 8
        self.height = 16
        self.image = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.rect.x = 16
        self.rect.y = 16
        self.have_image = False
        self.standing = False
        try:
            self.images = pygame.image.load(self.image_name)
            self.images.convert_alpha()
            self.images_num = 8
            self.image_c = 0
            self.have_image = True
        except pygame.error:
            self.image.fill((255, 255, 0))

    def move(self):
        self.keys_pressed = pygame.key.get_pressed()

        if self.keys_pressed[K_a]:
            self.rect.x -= self.speed
            if self.check_collision():
                self.rect.x += self.speed

        if self.keys_pressed[K_d]:
            self.rect.x += self.speed
            if self.check_collision():
                self.rect.x -= self.speed

        if self.y_vel < 4:
            self.y_vel += 0.1
            self.y_vel = round(self.y_vel, 1)

        if (self.keys_pressed[K_w] or self.keys_pressed[K_SPACE]) and self.standing:
            self.standing = False
            self.y_vel = -4
            """if self.keys_pressed[K_a] or self.keys_pressed[K_d]:
                self.y_vel -= 1"""

        self.rect.y += math.ceil(self.y_vel)
        if self.check_collision():
            self.rect.y -= self.y_vel
            if self.y_vel > 0:
                self.standing = True
            self.y_vel = 0
        else:
            self.standing = False

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, AllPlatforms) is not None:
            return True

    def render(self):

        # Image to use
        if self.have_image:
            if self.image_c >= self.images_num - 1:
                self.image_c = 0
            else:
                self.image_c += 1
            self.image.fill((255, 255, 255, 255))
            self.image.blit(self.images, (-(self.image_c * self.width), 0))
        # ((self.image_c * self.width), 0, self.width, self.height)
        return self.image


AllPlatforms = pygame.sprite.Group()
"""Makes Group for all platforms to make it easy to render"""


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((Platformer.TILESIZE, Platformer.TILESIZE))
        self.color = Platformer.BLACK
        self.rect = pygame.Rect(pos[0], pos[1], Platformer.TILESIZE, Platformer.TILESIZE)
        AllPlatforms.add(self)


class Level(object):
    def __init__(self, filename):
        self.parser = configparser.ConfigParser()
        self.parser.read(filename)
        self.map = list(self.parser.get("level", "map").split('\n'))
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.image = pygame.Surface(
            (self.width * Platformer.TILESIZE, self.height * Platformer.TILESIZE))

    def build_map(self):
        for map_y, line in enumerate(self.map):
            for map_x, c in enumerate(line):
                if c == "0":
                    Platform((map_x * Platformer.TILESIZE, map_y * Platformer.TILESIZE))

    def render_map(self):
        self.image.fill((255, 255, 255))
        AllPlatforms.draw(self.image)
        return self.image
