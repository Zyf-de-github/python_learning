import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game, x_offset, y_offset,x_speed=0):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.x_speed = x_speed

        self.x = float(self.rect.x+x_offset)
        self.y = float(self.rect.y+y_offset)
    def update(self):#重写函数
        self.y -= self.settings.bullet_speed
        self.x += self.x_speed
        self.rect.y = int(self.y)
        self.rect.x = int(self.x)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

