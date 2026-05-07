import pygame
import random
import math

class Bullet:
    def __init__(self, x, y, size, direction, momentum, damage, color):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.momentum = momentum
        self.damage = damage
        self.color = color

        self.hurtbox = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.hurtbox)
    def move(self, dx, dy):
        self.x += dx * self.direction[0] + self.momentum[0]
        self.y += dy * self.direction[1] + self.momentum[1]
    def interact(self, objects):
        for i in objects:
            if (self.hurtbox.colliderect(i.hitbox)):
                i.health -= self.damage
                if (i.health < 0):
                    objects.remove(i)
                self.x = 1000
                self.y = 1000
    def update(self, screen, dx, dy, objects):
        self.move(dx, dy)
        self.hurtbox = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
        self.interact(objects)
        self.draw(screen)