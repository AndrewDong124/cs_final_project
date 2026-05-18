import pygame
from entity import Entity
from player import Player
import random
import math

class Doppel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y; self.rel_y = y
        self.width = width
        self.height = height
        self.timer = 0

        self.position = []

        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = "#808080"

    def copy(self, player):
        if (self.timer < 30):
            self.timer += 1
            self.position.append(player.real_hitbox)
        else:
            self.color = "#FF0000"
            self.x = self.position[self.timer%30].x
            self.y = self.position[self.timer%30].y
            self.width = self.position[self.timer%30].width
            self.height = self.position[self.timer%30].height
            self.position[self.timer%30] = player.real_hitbox
            self.timer += 1
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.fake_hitbox)
    def move(self, dy):
        self.rel_y = self.y - dy + 275
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
    def update(self, dy, player, screen):
        self.copy(player)
        self.move(dy)
        self.draw(screen)