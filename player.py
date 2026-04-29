import pygame
from entity import Entity
import math

class Player(Entity):
    def __init__(self, x, y, height, width, max_speed, dx, dy, health, damage, color):
        super().__init__(x, y, height, width, max_speed, dx, dy, health, damage, color)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def move(self):
        if (abs(self.dx) < self.max_speed and abs(self.dy) < self.max_speed):
            