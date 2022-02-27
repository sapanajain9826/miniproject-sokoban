import queue
from copy import deepcopy
from time import time

from state_space import *


def create_state(my_game):
    """
    from the game board of pygame, read in the information to generate an object of the class State
    """
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
            if char == '+':
                man_position = [col_index, row_index]
                crate_destination.append([col_index, row_index])
            if char == '*':
                crate_position.append([col_index, row_index])
                crate_destination.append([col_index, row_index])
            if char == '$':
                crate_position.append([col_index, row_index])
            if char == '.':
                crate_destination.append([col_index, row_index])
            if char == '#':
                wall_position.append([col_index, row_index])
        # sys.stdout.write('\n')
    return State(crate_position, man_position, wall_position, crate_destination, [])


def search(my_game):
    """
        Breadth first search algorithm
    """
    start = time()
    nodes_generated = 0
    nodes_repeated = 0
    game_state = create_state(my_game)
    print(game_state.__dict__)
    if game_state.is_game_complete():
        end = time()
        print_results(my_game, 1, 0, 0, 1, end - start)
        return my_game
    node = game_state
    nodes_generated += 1
    frontier = queue.LifoQueue()
    frontier.put_nowait(node)
    explored = set()
    keep_looking = True
    while keep_looking:
        if frontier.empty():
            print("Solution not found")
            return
        else:
            curr_node = frontier.get_nowait()
            moves = curr_node.get_possible_moves()
            crate_position_a = set()
            for a in curr_node.crate_position:
                crate_position_a.add(tuple(a))
            curr_node.crate_position_hash = frozenset(crate_position_a)
            explored.add(curr_node)
            for m in moves:
                child = deepcopy(curr_node)
                nodes_generated += 1
                child.move(m)
                if child not in explored:
                    if child.is_game_complete():
                        end = time()
                        print_results(child, nodes_generated, nodes_repeated,
                                      frontier.qsize(), len(explored), end - start)
                        return child
                    frontier.put_nowait(child)
                else:
                    nodes_repeated += 1


def test_basic_structure(my_game):
    game_state = create_state(my_game)
    print(game_state.is_game_complete())
    print(game_state.__dict__)
    game_state.move('d')
    print(game_state.__dict__)
    game_state.move('r')
    game_state.move('r')
    print(game_state.__dict__)
    print(game_state.print_directions())
    print(game_state.get_possible_moves())
    return 1
