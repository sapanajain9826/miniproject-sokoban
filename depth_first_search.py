import sys

from state_space import *

import numpy as np
from sokoban import *


def create_initial_state(mygame):
    row_index = 0
    crate_position = []
    crate_destination = []
    wall_position = []
    man_position = []
    for row in mygame.matrix:
        row_index = row_index + 1
        col_index = 0
        for char in row:
            col_index = col_index + 1
            sys.stdout.write(char)
            sys.stdout.flush()
            if char == '@':
                man_position = [col_index, row_index]
                # print(man_position)
            if char == '$':
                crate_position.append([col_index, row_index])
                # print(crate_position)
            if char == '.':
                crate_destination.append([col_index, row_index])
                # print(crate_destination)
            if char == '#':
                wall_position.append([col_index, row_index])
                # print(wall_position)
        sys.stdout.write('\n')
    return InitialState(crate_position, man_position, wall_position, crate_destination)


def get_new_position(old_position, move):
    if move == 'l':
        new_position = [old_position[0] - 1, old_position[1]]
    elif move == 'r':
        new_position = [old_position[0] + 1, old_position[1]]
    elif move == 'u':
        new_position = [old_position[0], old_position[1] - 1]
    elif move == 'd':
        new_position = [old_position[0], old_position[1] + 1]
    else:
        print('invalid move')
        new_position = old_position
    return new_position


def is_position_empty(game_initial_state, move, man_current_position):
    future_position = get_new_position(man_current_position, move)
    # print('future position' + str(future_position))
    if future_position in game_initial_state.wall_position:
        # print('wall present')
        return False
    elif future_position in game_initial_state.crate_position:
        # print('checking crate')
        if is_position_empty(game_initial_state, move, future_position):
            return True
        else:
            return False
    else:
        return True


def check_move_legal(current_state, move, game_initial_state):
    """
    move is legal if the man or crate new position is empty
    """
    man_position = current_state.man_position[0]
    # print('man position' + str(man_position))
    if is_position_empty(game_initial_state, move, man_position):
        return True
    else:
        return False


def get_possible_moves(current_state, game_initial_state):
    for move in ['l', 'r', 'u', 'd']:
        if check_move_legal(current_state, move, game_initial_state):
            print('legal move ' + move)
        else:
            print('not legal move ' + move)
    print('I came here')
    return 1


def auto_solve_dfs(mygame):
    game_initial_state = create_initial_state(mygame)
    game_final_state = FinalState(game_initial_state.man_position, game_initial_state.wall_position,
                                  game_initial_state.crate_destination)
    # print(game_initial_state.__dict__)
    # print(game_final_state.__dict__)
    number_of_moves = 0
    current_state = State(game_initial_state.crate_position, game_initial_state.man_position)
    get_possible_moves(current_state, game_initial_state)
    # game_current_state = State(game_initial_state.crate_position, game_initial_state.man_position,)
    print('algo complete')
    return 1
