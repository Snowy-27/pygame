import pygame
from player import Player

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.pressed = {}
