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
    running = True
    player_dx = 0
    player_dy = 0
    wFlag = False; sFlag = False; dFlag = False; aFlag = False
    player = Player(100, 100, 25, 25, 10, 100, 5, "#FFFFFF")

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    wFlag = True
                if event.key == pygame.K_a:
                    aFlag = True
                if event.key == pygame.K_s:
                    sFlag = True
                if event.key == pygame.K_d:
                    dFlag = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    wFlag = False
                    sFlag = False
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    aFlag = False
                    dFlag = False
        if (wFlag):
            player_dy = player_dy - 2
            if (player_dy <= -10):
                player_dy = -10
        if (sFlag):
            player_dy = player_dy + 2
            if (player_dy >= 10):
                player_dy = 10
        if (aFlag):
            player_dx = player_dx - 2
            if (player_dx <= -10):
                player_dx = -10
        if (dFlag): 
            player_dx = player_dx + 2
            if (player_dx >= 10):
                player_dx = 10
        if (player_dx != 0):
            player_dx -= abs(player_dx)/player_dx
        if (player_dy != 0):
            player_dy -= abs(player_dy)/player_dy

        player.update(screen, player_dx, player_dy)
        

        pygame.display.update()
        clock.tick(FPS)

    

if __name__ == "__main__":
    main()
    pygame.quit()