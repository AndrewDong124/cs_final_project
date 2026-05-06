import pygame
from entity import Entity
from player import Player
import math

class Enemy(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        super().__init__(x, y, height, width, max_speed, health, damage, color)
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
    def move(self, player, top, bottom, right, left):
        dx, dy = (player.x - self.x, player.y - self.y)
        self.x += dx/25
        self.y += dy/25
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
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.hitbox)
    def damage_calculation(self, damage):
        self.health -= damage
    def update(self, screen, player):
        self.draw(screen)
        self.move(player, 10, 590, 10, 890)