from state_space import *


def create_state(my_game):
    row_index = 0
    crate_position = []
    crate_destination = []
    wall_position = []
    man_position = []
    for row in my_game.matrix:
        row_index = row_index + 1
        col_index = 0
        for char in row:
            col_index = col_index + 1
            # sys.stdout.write(char)
            # sys.stdout.flush()
            if char == '@':
                man_position = [col_index, row_index]
            if char == '$':
                crate_position.append((col_index, row_index))
            if char == '.':
                crate_destination.append((col_index, row_index))
            if char == '#':
                wall_position.append((col_index, row_index))
        # sys.stdout.write('\n')
    return State(crate_position, man_position, wall_position, crate_destination)


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


def is_position_empty(game_state, move, man_current_position):
    future_position = get_new_position(man_current_position, move)
    if future_position in game_state.wall_position:
        return False
    elif future_position in game_state.crate_position:
        if is_position_empty(game_state, move, future_position):
            return True
        else:
            return False
    else:
        return True


def check_move_legal(game_state, move):
    """
    move is legal if the man or crate new position is empty
    """
    man_position = game_state.man_position
    if is_position_empty(game_state, move, man_position):
        return True
    else:
        return False


def get_possible_moves(game_state):
    moves =[]
    for m in ['l', 'r', 'u', 'd']:
        if check_move_legal(game_state, m):
            moves.append(m)
            # print('legal move ' + m)
        else:
            pass
            # print('not legal move ' + m)a
    return moves


def auto_solve_dfs(my_game):
    game_state = create_state(my_game)
    number_of_moves = 0
    print(get_possible_moves(game_state))

    print('Good job ! Algorithm Complete')
    return 1
