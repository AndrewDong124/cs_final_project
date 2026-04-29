import pygame
import sys
import random
from entity import Entity
from player import Player

# constants
WIDTH = 900
HEIGHT = 600
FPS = 30

BG_COLOR = "#000000"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def main():
    screen.fill(BG_COLOR)

    player = Player(100, 100, 25, 25, 0, 0, 10, 100, 5, "#FFFFFF")

    pygame.display.update()
    clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()