import pygame
from entity import Entity
import threading
import math

class Player(Entity):
    def __init__(self, x, y, height, width, max_speed, health, damage, color, dx = 0, dy = 0):
        super().__init__(x, y, height, width, max_speed, health, damage, color)
        self.dx = dx
        self.dy = dy
        self.grounded = False
        self.gravity = 0.8
        self.jump_counter = 0
        self.dash_counter = 0
        self.rel_y = 300-self.height
        self.camera_y = self.y
        self.hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
        self.real_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x, self.rel_y, self.width, self.height)
        self.real_hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.hitbox)
    
    def y_detection(self, i):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.hitbox.colliderect(i.hitbox):
            if self.dy > 0:
                self.hitbox.bottom = i.hitbox.top
                self.y = self.hitbox.top
                self.dy = 0
                self.grounded = True
                self.jump_counter = 0
                self.dash_counter = 0
            if self.dy < 0:
                self.hitbox.top = i.hitbox.bottom
                self.y = self.hitbox.top
                self.dy = 0
        else:
            self.grounded = False
    def x_detection(self, i):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.hitbox.colliderect(i.hitbox):
            if self.dx > 0:
                self.hitbox.right = i.hitbox.left
                self.x = self.hitbox.left
            if self.dx < 0:
                self.hitbox.left = i.hitbox.right
                self.x = self.hitbox.left



    # Source - https://stackoverflow.com/a/74333777
    # Posted by Rabbid76
    # Retrieved 2026-05-14, License - CC BY-SA 4.0
    def move(self, objects):
        self.y += self.dy
        for i in objects:
            self.y_detection(i)

        self.x += self.dx
        for i in objects:
            self.x_detection(i)

    def jump(self, velocity):
        if (not self.grounded and (self.jump_counter >= 2)):
            return True
        self.dy = -velocity
        self.grounded = False
        self.jump_counter += 1

    def fall(self):
        if (self.grounded):
            return True
        self.dy += self.gravity
        self.y += self.dy
    def dash(self, dash_x, dash_y, direction, dash_time, objects):
        if (self.dash_counter <= 1):
            if (dash_time >= 4 and dash_time < 5):
                self.dx /= 3
                self.dy /= 3
                return True
            if (dash_time >= 5):
                self.gravity = 1
                self.dash_counter += 1
                return False
            self.gravity = 0
            self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
            if (direction[0] != 0 and direction[1] != 0):
                self.dy = dash_y * direction[1]/1.41
                self.dx = dash_x * direction[0]/1.41
            else:
                self.dy = dash_y * direction[1]
                self.dx += dash_x * direction[0]
            self.y += self.dy
            for i in objects:
                self.y_detection(i)
            self.x += self.dx
            for i in objects:
                self.x_detection(i)
            return True

    def damage_calculation(self, object):
        if (self.hitbox.colliderect(object.fake_hitbox)):
            return True
    def update(self, screen, floor, objects):
        self.fall()
        self.move(floor)
        self.draw(screen)
        for i in objects:
            i.move(self.y)

        