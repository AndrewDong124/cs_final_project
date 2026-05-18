import pygame
from entity import Entity
from player import Player
import random
import math

class Hand():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.x = 0; self.y = 500
        self.rel_y = self.y
        self.height = 1000
        self.min_speed = 0.5

        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, 1500, self.height)
        self.hitbox = pygame.Rect(self.x, self.y, 1500, self.height)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.fake_hitbox)
    def move(self, dy):
        self.y -= self.speed
        self.rel_y = self.y - dy + 275
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, 1500, self.height)
    def update(self, screen, dy, player):
        self.draw(screen)
        self.move(dy)
        self.multiplier = max((self.y - player.y)/80, self.min_speed)
        self.min_speed += 0.002
        self.speed = self.multiplier
