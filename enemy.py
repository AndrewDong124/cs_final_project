import pygame
from entity import Entity
from player import Player
import random
import math

class Enemy(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        super().__init__(x, y, height, width, max_speed, health, damage, color)

        self.rel_y = self.y
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, player, top, bottom, right, left, objects, speed):
        steps_number = max(abs(player.x-self.x)/speed, abs(player.y-self.y)/speed)

        step_x = float(player.x-self.x)/steps_number
        step_y = float(player.rel_y-self.rel_y)/steps_number

        self.x += step_x
        self.y += step_y

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
        for i in objects:
            if (i != self and self.hitbox.colliderect(i.hitbox)):
                if (self.x - i.x >= 0):
                    self.x += 1
                else:
                    self.x -= 1
                if (self.y -i.y >= 0):
                    self.y += 1
                else:
                    self.y -= 1
        self.rel_y = self.y + 275
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.fake_hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)

        pygame.draw.rect(screen, self.color, self.hitbox)
        pygame.draw.rect(screen, "#1A1A1A", self.fake_hitbox)
    def damage_calculation(self, damage):
        self.health -= damage
        self.x = random.randint(10, 590)
        self.y = random.randint(10, 890)
    def update(self, screen, player, objects, speed):
        self.draw(screen)
        self.move(player, 10, 590, 10, 890, objects, speed)