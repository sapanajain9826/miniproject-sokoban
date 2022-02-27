"""
This is an automated sokoban agent
"""
import sys

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

sleep_time = 0.75
game_state = []
automatic_player = False


def create_gen(moves_list):
    """
    generator to get moves to show automated play
    """
    for my_key in moves_list:
        yield my_key


while 1:
    if game.is_completed():
        sokoban.display_end(screen)
    sokoban.print_game(game.get_matrix(), screen)
    solution =[]
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
                game_state = search(game)
                solution = (my_key for my_key in game_state.list_of_moves)
                automatic_player = True
                break
    while automatic_player:
        try:
            sokoban.print_game(game.get_matrix(), screen)
            pygame.display.update()
            pygame.time.delay(50)
            key = next(solution)
            if game.is_completed():
                sokoban.display_end(screen)
            if key == 'l':
                game.move(-1, 0, True)
            elif key == 'r':
                game.move(1, 0, True)
            elif key == 'u':
                game.move(0, -1, True)
            elif key == 'd':
                game.move(0, 1, True)
        except StopIteration:
            automatic_player = False
            print('game completed')
            break
    pygame.display.update()
