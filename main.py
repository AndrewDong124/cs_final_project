import pygame
import sys
import random
from entity import Entity
from player import Player
from doppel import Doppel
from floor import Floor
from hand import Hand
import os

# constants
WIDTH = 1200
HEIGHT = 600
FPS = 30
BG_COLOR = "#000000"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('arial', 22)
pygame.display.set_caption("Celeste?")
clock = pygame.time.Clock()

def main():
    running = True

    enemy_list = []
    in_dash = False
    direction = [0, 0]
    wFlag = False; sFlag = False; dFlag = False; aFlag = False
    player = Player(100, 700, 25, 25, 100, 100, 1, "#FFFFFF")
    attack_cooldown = 0; dash_time = 0

    hand = Hand(1, "#FF0000"); enemy_list.append(hand)
    # doppel = Doppel(0, 0, 0, 0)

    border_list = []
    floor_list = []
    bottom_border = Floor(0, HEIGHT-300, WIDTH, 1000, "#FFFFFF"); floor_list.append(bottom_border)
    left_border = Floor(-1002, -10000, 1000, 11000, "#FFFFFF"); border_list.append(left_border)
    right_border = Floor(WIDTH, -10000, 1000, 11000, "#FFFFFF"); border_list.append(right_border)


    combined_list = floor_list + border_list
    block_y = 4

    for i in range(50):
        floor_selection = random.randint(1, 20)
        if (floor_selection > 9):
            for j in range(40):
                block = Floor(random.randrange(0, WIDTH-50, 50), random.randrange((block_y-10) * 50, block_y * 50, 50), 50, 50, "#FF00FF")
                floor_list.append(block)
            block_y -= 10
        else:
            file_name = "structures/struct" + str(floor_selection) + ".txt"
            block_generation = open(file_name, "r")
            line = block_generation.readline().strip()
            while (line != ""):
                line = block_generation.readline().strip()
                for i in range(len(line)):
                    if (line[i] == "#"):
                        block = Floor(i*50, block_y * 50, 50, 50, "#FF00FF")
                        floor_list.append(block)
                block_y -= 1
            block_generation.close()

    # floor1 = open("structures/struct1.txt", "r")
    # line = floor1.readline().strip()
    # while (line != ""):
    #     line = floor1.readline().strip()
    #     for i in range(len(line)):
    #         if (line[i] == "#"):
    #             block = Floor(i*50, block_y * 50, 50, 50, "#FF00FF")
    #             floor_list.append(block)
    #     block_y -= 1
    # floor1.close()

    while running:
        screen.fill(BG_COLOR)
        height = round(-(player.y + 325)/50, 2)
        height_text = f"height: {height}m"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    player.jump(9.5)
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
                if event.key == pygame.K_x:
                    in_dash =  player.dash(18, 18, direction, dash_time, combined_list)
                    player.dy = 0
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

        combined_list = floor_list + border_list
        player.update(screen, combined_list, floor_list)

        if (in_dash == True):
            dash_time += 1
            in_dash = player.dash(25, 25, direction, dash_time, combined_list)
        else:
            dash_time = 0
        
        attack_cooldown += 1

        for i in border_list:
            i.draw(screen)
        for i in floor_list:
            i.draw(screen)
        
        hand.update(screen, player.y, player)
        if (player.damage_calculation(hand)):
            running = False
        # doppel.update(player.y, player, screen)
        # if (player.damage_calculation(doppel)):
        #     running = False

        text_surface = font.render(height_text, True, "#FFFFFF")
        screen.blit(text_surface, (WIDTH/2-50, 20))


        pygame.display.update()
        clock.tick(FPS)

    

if __name__ == "__main__":
    main()
    pygame.quit()