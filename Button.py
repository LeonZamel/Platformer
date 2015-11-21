from Platformer import *
import main


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
