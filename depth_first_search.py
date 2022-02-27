import queue
from copy import deepcopy
from time import time

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


# def searchold(board):
#     start = time()
#     nodes_generated = 0
#     nodes_repeated = 0
#     if board.is_win():
#         end = time()
#         print_results(board, 1, 0, 0, 1, end - start)
#         return board
#     node = deepcopy(board)
#     nodes_generated += 1
#     frontier = MyQueue()
#     frontier.push(node)
#     explored = set()
#     keepLooking = True
#     while keepLooking:
#         if frontier.isEmpty():
#             print "Solution not found"
#             return
#         else:
#             currNode = frontier.pop()
#             moves = currNode.moves_available()
#             currNode.fboxes = frozenset(currNode.boxes)
#             explored.add(currNode)
#             for m in moves:
#                 child = deepcopy(currNode)
#                 nodes_generated += 1
#                 child.move(m)
#                 if child not in explored:
#                     if child.is_win():
#                         end = time()
#                         print_results(child, nodes_generated, nodes_repeated, len(
#                                       frontier), len(explored), end - start)
#                         return child
#                     frontier.push(child)
#                 else:
#                     nodes_repeated += 1

def search(my_game):
    start = time()
    nodes_generated = 0
    nodes_repeated = 0
    game_state = create_state(my_game)
    # game_initial_state = game_state
    # print(game_state.is_game_complete())
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
    keepLooking = True
    while keepLooking:
        if frontier.empty():
            print("Solution not found")
            return
        else:
            currNode = frontier.get_nowait()
            moves = currNode.get_possible_moves()
            crate_position_a = set()
            for a in currNode.crate_position:
                crate_position_a.add(tuple(a))
            currNode.crate_position_hash = frozenset(crate_position_a)
            explored.add(currNode)
            for m in moves:
                # print('m ' + m + 'node gen ' + str(nodes_generated))
                child = deepcopy(currNode)
                nodes_generated += 1
                # print(child.print_directions())
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
    print(game_state.get_possible_moves())
    print('Good job ! Algorithm Complete')
    return 1
