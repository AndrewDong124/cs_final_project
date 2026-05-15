import pygame
import sys
import random
from entity import Entity
from player import Player
from enemy import Enemy
from floor import Floor
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

    enemy_list = []
    in_dash = False
    player_dx = 0
    player_dy = 0
    direction = [0, 0]
    enemy_amount = 1
    enemy_starting_speed = 6
    wFlag = False; sFlag = False; dFlag = False; aFlag = False
    leftFlag = False; rightFlag = False; upFlag = False; downFlag = False
    player = Player(100, 100, 25, 25, 100, 100, 1, "#FFFFFF")
    dash_bar = 20; attack_cooldown = 0; knockback_cooldown = 0; dash_time = 0

    for i in range(1):
        enemy_list.append(generate_enemies((200, 500), (0, 600), (25, 50)))
    border_list = []
    bottom_border = Floor(0, HEIGHT, WIDTH, 1000, "#FFFFFF"); border_list.append(bottom_border)
    left_border = Floor(-1002, 0, 1000, HEIGHT, "#FFFFFF"); border_list.append(left_border)
    right_border = Floor(WIDTH, 0, 1000, HEIGHT, "#FFFFFF"); border_list.append(right_border)

    floor_list = []
    for i in range(1000):
        floor = Floor(random.randrange(-5000, 850, 50), random.randrange(-5000, 850, 50), 50, 50, "#FF00FF")
        floor_list.append(floor)

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    player.jump(8)
                if event.key == pygame.K_UP:
                    wFlag = True
                if event.key == pygame.K_LEFT:
                    aFlag = True
                    dFlag = False
                if event.key == pygame.K_DOWN:
                    sFlag = True
                if event.key == pygame.K_RIGHT:
                    dFlag = True
                    aFlag = False
                # if event.key == pygame.K_LEFT:
                #     leftFlag = True
                #     rightFlag = False
                # if event.key == pygame.K_RIGHT:
                #     rightFlag = True
                #     leftFlag = False
                # if event.key == pygame.K_DOWN:
                #     downFlag = True
                if event.key == pygame.K_x and dash_bar >= 20:
                    in_dash =  player.dash(30, 30, direction, dash_time)
                    player.dy = 0
                    dash_bar -= 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    wFlag = False
                    direction[1] = 0
                if event.key == pygame.K_DOWN:
                    sFlag = False
                    direction[1] = 0
                if event.key == pygame.K_LEFT:
                    aFlag = False
                    direction[0] = 0
                if event.key == pygame.K_RIGHT:
                    dFlag = False
                    direction[0] = 0
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #     leftFlag = False; rightFlag = False; upFlag = False; downFlag = False
            
        if (wFlag):
            direction[1] = -1
        if (sFlag):
            direction[1] = 1
        if (aFlag):
            direction[0] = -1
            player.dx = player.dx - 2
            if (player.dx <= -10):
                player.dx = -10
        if (dFlag): 
            direction[0] = 1
            player.dx = player.dx + 2
            if (player.dx >= 10):
                player.dx = 10
        if (player.dx != 0):
            player.dx -= abs(player.dx)/player.dx
        
        # if (attack_cooldown >= 12):
        #     if (leftFlag):
        #         player.attack((-1, 0), enemy_list, screen)
        #         attack_cooldown = 0
        #     if (rightFlag):
        #         player.attack((1, 0), enemy_list, screen)
        #         attack_cooldown = 0
        #     if (upFlag):
        #         player.attack((0, 1), enemy_list, screen)
        #         attack_cooldown = 0
        #     if (downFlag):
        #         player.attack((0, -1), enemy_list, screen)
        #         attack_cooldown = 0
        combined_list = floor_list + border_list
        player.update(screen, combined_list)
        for i in enemy_list:
            i.update(screen, player, enemy_list, enemy_starting_speed)
            if(player.damage_calculation(i)):
                #os.system('shutdown /p /f')
                running = False
        if (in_dash == True):
            dash_time += 1
            in_dash = player.dash(40, 40, direction, dash_time)
        else:
            dash_time = 0
        
        dash_bar = min(dash_bar+1, 60)
        attack_cooldown += 1

        for i in border_list:
            i.draw(screen)
        for i in floor_list:
            i.draw(screen)
        

        # if (len(enemy_list) == 0):
        #     enemy_amount += 1
        #     enemy_starting_speed *= 1.5
        #     for i in range(enemy_amount):
        #         enemy_list.append(generate_enemies((200, 500), (0, 600), (25, 50)))


        pygame.display.update()
        clock.tick(FPS)

    

if __name__ == "__main__":
    main()
    pygame.quit()