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
                crate_position.append([col_index, row_index])
            if char == '.':
                crate_destination.append([col_index, row_index])
            if char == '#':
                wall_position.append([col_index, row_index])
        # sys.stdout.write('\n')
    return State(crate_position, man_position, wall_position, crate_destination, [])





def test_basic_structure(my_game):
    game_state = create_state(my_game)
    game_initial_state = game_state
    print(game_state.is_game_complete())
    print(game_state.__dict__)
    game_state.move('d')
    print(game_state.__dict__)
    game_state.move('r')
    game_state.move('r')
    print(game_state.__dict__)
    print(game_state.print_directions())
    number_of_moves = 0
    print(get_possible_moves(game_state))
    print('Good job ! Algorithm Complete')
    return 1
