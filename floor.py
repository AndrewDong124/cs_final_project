import pygame
from entity import Entity
from player import Player

class Floor:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rel_y = self.y
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.fake_hitbox)
    def move(self, dy):
        self.rel_y = self.y - dy + 275
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)