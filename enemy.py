import pygame
from entity import Entity
from player import Player
import math

class Enemy(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        super().__init__(x, y, height, width, max_speed, health, damage, color)
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
    def move(self, player):
        x_distance = player.x - self.x
        y_distance = player.y - self.y
        if (y_distance != 0):
            ratio = x_distance/y_distance
        self.x += ratio * x_distance*0.01
        self.y += -5-(ratio*x_distance)*0.01
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.hitbox)
    def damage_calculation(self, damage):
        self.health -= damage
    def update(self, screen, player):
        self.draw(screen)
        self.move(player)