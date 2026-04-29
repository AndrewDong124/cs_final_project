import pygame

class Entity:
    def __init__(self, x, y, height, width, max_speed, dx, dy, health, damage, color):
        self.x = x
        self.y = y
        self.speed = max_speed
        self.dx = dx
        self.dy = dy
        self.health = health
        self.height = height
        self.width = width
        self.damage = damage
        self.color = color
        
        self.hitbox = pygame.Rect(x-width/2, y-height/2, width, height)