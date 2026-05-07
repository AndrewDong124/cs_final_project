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
        self.x += dx + self.momentum[0]
        self.y += dy + self.momentum[1]
    def interact(self, objects):
        self.hurtbox = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
        for i in objects:
            if (self.hurtbox.colliderect(i.hitbox)):
                objects.remove(i)
    def update(self, screen, dx, dy, objects):
        self.move(dx, dy)
        self.hurtbox = pygame.Rect(self.x-self.size/2, self.y-self.size/2, self.size, self.size)
        self.interact(objects)
        self.draw(screen)