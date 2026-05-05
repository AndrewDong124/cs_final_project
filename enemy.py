import pygame
from entity import Entity
from player import Player
import math

class Enemy(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        super().__init__(x, y, height, width, max_speed, health, damage, color)
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
    def move(self, max_speed):
        self.x += max_speed
        self.y += max_speed
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x-self.width/2, self.y-self.height/2, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.hitbox)
    def damage_calculation(self, player):
        if (self.hitbox.colliderect(player.hurtbox)):
            self.health -= player.damage
    def update(self, screen):
        self.draw(screen)
        self.move(-4.5)