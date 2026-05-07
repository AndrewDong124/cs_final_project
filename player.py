import pygame
from entity import Entity
from bullet import Bullet
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
    def dash(self, dash_x, dash_y, top, bottom, right, left, direction):
        self.x += dash_x * direction[0]
        self.y += dash_y * direction[1]
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
    def attack(self, direction, objects, projectile_list, dx, dy):
        projectile = Bullet(self.x, self.y, 15, direction, (dx, dy), 1, "#00FF00")
        projectile_list.append(projectile)
            
    def damage_calculation(self, object):
        if (self.hitbox.colliderect(object.hitbox)):
            return True
    def update(self, screen, dx, dy):
        self.move(dx, dy, 10, 590, 10, 890)
        self.draw(screen)