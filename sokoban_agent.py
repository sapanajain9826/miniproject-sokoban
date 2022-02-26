"""
This is an automated sokoban agent
"""
import sys
import time

import pygame

import sokoban
from depth_first_search import *


print("Start Game")

pygame.init()
pygame.display.set_caption("My Sokoban Game")
level = sokoban.start_game()
game = sokoban.Game('levels', level)
size = game.load_size()
screen = pygame.display.set_mode(size)

while 1:
    if game.is_completed():
        sokoban.display_end(screen)
    sokoban.print_game(game.get_matrix(), screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.move(0, -1, True)
            elif event.key == pygame.K_DOWN:
                game.move(0, 1, True)
            elif event.key == pygame.K_LEFT:
                game.move(-1, 0, True)
            elif event.key == pygame.K_RIGHT:
                game.move(1, 0, True)
            elif event.key == pygame.K_q:
                sys.exit(0)
            elif event.key == pygame.K_d:
                game.undo_move()
            elif event.key == pygame.K_a:
                # time.sleep(0.1)
                # game.move(0, -1, True)
                # pygame.display.update()
                # time.sleep(5)
                # game.move(1, 0, True)
                # game.print_matrix()
                test_basic_structure(game)
    pygame.display.update()


