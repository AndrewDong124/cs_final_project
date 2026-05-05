import pygame
from entity import Entity
import math

class Player(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        super().__init__(x, y, height, width, max_speed, health, damage, color)
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.hitbox)
    def move(self, dx, dy, top, bottom, right, left):
        self.x += dx
        self.y += dy
        if (self.x > left):
            self.x = left
            dx = 0
        if (self.x < right):
            self.x = right
            dx = 0
        if (self.y < top):
            self.y = top
            dy = 0
        if (self.y > bottom):
            self.y = bottom
            dy = 0
    def damage_calculation(self, object):
        if (self.hitbox.colliderect(object.hitbox)):
            return True
    def update(self, screen, dx, dy):
        self.move(dx, dy, 10, 590, 10, 890)
        self.draw(screen)