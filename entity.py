import pygame

class Entity:
    def __init__(self, x, y, height, width, max_speed, health, damage, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = max_speed
        self.health = health
        self.damage = damage
        self.color = color