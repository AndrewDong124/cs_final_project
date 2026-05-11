import pygame
import sys
import random
from entity import Entity
from player import Player
from enemy import Enemy
from bullet import Bullet
import os

# constants
WIDTH = 900
HEIGHT = 600
FPS = 30

BG_COLOR = "#000000"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def generate_enemies(x_range, y_range, size_range):
    x_pos = random.randint(x_range[0], x_range[1])
    y_pos = random.randint(y_range[0], y_range[1])
    size = random.randint(size_range[0], size_range[1])
    new_enemy = Enemy(x_pos, y_pos, size, size, 0, 5, 0, "#FF0000")
    return new_enemy

def main():
    running = True
    bullet = Bullet(450, 450, 50, [0, 1], (0, 0), 5, "#00FF00")

    enemy_list = []
    projectile_list = []
    player_dx = 0
    player_dy = 0
    direction = [0, 0]
    enemy_amount = 1
    enemy_starting_speed = 1
    wFlag = False; sFlag = False; dFlag = False; aFlag = False
    leftFlag = False; rightFlag = False; upFlag = False; downFlag = False
    player = Player(100, 100, 25, 25, 100, 100, 1, "#FFFFFF")
    dash_cooldown = 20; attack_cooldown = 0

    for i in range(1):
        enemy_list.append(generate_enemies((200, 500), (0, 600), (25, 50)))

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
                if event.key == pygame.K_LEFT:
                    leftFlag = True
                if event.key == pygame.K_RIGHT:
                    rightFlag = True
                if event.key == pygame.K_UP:
                    upFlag = True
                if event.key == pygame.K_DOWN:
                    downFlag = True
                if event.key == pygame.K_LSHIFT and dash_cooldown > 20:
                    player.dash(100, 100, 10, 590, 10, 890, direction)
                    dash_cooldown = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    wFlag = False
                    sFlag = False
                    direction[1] = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    aFlag = False
                    dFlag = False
                    direction[0] = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    leftFlag = False; rightFlag = False; upFlag = False; downFlag = False
        if (wFlag):
            direction[1] = -1
            player_dy = player_dy - 2
            if (player_dy <= -10):
                player_dy = -10
        if (sFlag):
            direction[1] = 1
            player_dy = player_dy + 2
            if (player_dy >= 10):
                player_dy = 10
        if (aFlag):
            direction[0] = -1
            player_dx = player_dx - 2
            if (player_dx <= -10):
                player_dx = -10
        if (dFlag): 
            direction[0] = 1
            player_dx = player_dx + 2
            if (player_dx >= 10):
                player_dx = 10
        if (player_dx != 0):
            player_dx -= abs(player_dx)/player_dx
        if (player_dy != 0):
            player_dy -= abs(player_dy)/player_dy
        
        if (attack_cooldown >= 12):
            if (leftFlag):
                player.attack((-1, 0), enemy_list, projectile_list, player_dx, player_dy)
                attack_cooldown = 0
            if (rightFlag):
                player.attack((1, 0), enemy_list, projectile_list, player_dx, player_dy)
                attack_cooldown = 0
            if (upFlag):
                player.attack((0, -1), enemy_list, projectile_list, player_dx, player_dy)
                attack_cooldown = 0
            if (downFlag):
                player.attack((0, 1), enemy_list, projectile_list, player_dx, player_dy)
                attack_cooldown = 0
        player.update(screen, player_dx, player_dy)
        for i in enemy_list:
            i.update(screen, player, enemy_list, enemy_starting_speed)
            if(player.damage_calculation(i)):
                #os.system('shutdown /p /f')
                running = False
        if (len(projectile_list) != 0):
            for i in projectile_list:
                i.update(screen, 10, 10, enemy_list)
        
        dash_cooldown += 1
        attack_cooldown += 1

        if (len(enemy_list) == 0):
            enemy_amount += 1
            enemy_starting_speed *= 1.5
            for i in range(enemy_amount):
                enemy_list.append(generate_enemies((200, 500), (0, 600), (25, 50)))
             


        pygame.display.update()
        clock.tick(FPS)

    

if __name__ == "__main__":
    main()
    pygame.quit()