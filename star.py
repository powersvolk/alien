import pygame
from pygame.sprite import Sprite
from random import randint
class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.top > self.settings.screen_height:
            self.rect.y = randint(-100, -10) 
            self.rect.x = randint(0, self.settings.screen_width) 
