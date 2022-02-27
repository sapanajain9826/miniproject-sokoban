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


def is_position_empty(game_state, move, current_position):
    crate_moved = False
    future_position = get_new_position(current_position, move)
    if future_position in game_state.wall_position:
        return False, crate_moved
    elif future_position in game_state.crate_position:
        crate_moved = True
        if is_position_empty(game_state, move, future_position)[0]:
            return True, crate_moved
        else:
            return False, crate_moved
    else:
        return True, crate_moved


def check_move_legal(game_state, move):
    """
    move is legal if the man or crate new position is empty
    """
    if is_position_empty(game_state, move, game_state.man_position)[0]:
        return True
    else:
        return False


class UniqueSubState:
    def __init__(self, crate_position, man_position):
        self.crate_position = set()
        self.man_position = man_position
        self.crate_position_hash = frozenset()

    def add_box(self, position):
        self.crate_position.add(position)


class State:

    def __init__(self, crate_position, man_position, wall_position, crate_destination, list_of_moves):
        self.list_of_moves = list_of_moves
        self.crate_position = crate_position
        self.man_position = man_position
        self.crate_destination = crate_destination
        self.wall_position = wall_position
        self.crate_position_a = set()
        for a in crate_position:
            self.crate_position_a.add(tuple(a))
        self.crate_position_hash = frozenset(self.crate_position_a)

    def move(self, direction):
        position_empty, crate_moved = is_position_empty(self, direction, self.man_position)
        if check_move_legal(self, direction):
            if position_empty:
                if crate_moved:
                    crate_index = self.crate_position.index(get_new_position(self.man_position, direction))
                    self.crate_position[crate_index] = get_new_position(self.crate_position[crate_index], direction)
                    self.man_position = get_new_position(self.man_position, direction)
                    self.list_of_moves.append(direction)
                else:
                    self.man_position = get_new_position(self.man_position, direction)
                    self.list_of_moves.append(direction)
        else:
            print('illegal move')
            return False

    def is_game_complete(self):
        if sorted(self.crate_position) == sorted(self.crate_destination):
            return True
        else:
            return False

    def print_directions(self):
        chars = ''
        for d in self.list_of_moves:
            chars += d
            chars += ', '
        return chars

    def get_possible_moves(self):
        moves = []
        for m in ['l', 'r', 'u', 'd']:
            if check_move_legal(self, m):
                moves.append(m)
                # print('legal move ' + m)
            else:
                pass
                # print('not legal move ' + m)a
        return moves

    def generate_sub_state(self):
        return UniqueSubState(self.crate_position, self.man_position)

    def __hash__(self):
        return hash((self.crate_position_hash, tuple(self.man_position)))

    def __eq__(self, other):
        if sorted(self.crate_position) == sorted(other.crate_position) and sorted(self.man_position) == sorted(other.man_position):
            return True
        else:
            return False


def print_results(board, gen, rep, fri, expl, dur):
    print("\n1. Breadth-first search")
    print("Solution: " + board.print_directions())
    print("Nodes generated: " + str(gen))
    print("Nodes repeated: " + str(rep))
    print("Fringe nodes: " + str(fri))
    print("Explored nodes: " + str(expl))
    print('Duration: ' + str(dur) + ' secs')
