# class State:
#
#     def __init__(self, crate_position, man_position, last_move=0, current_moves=0):
#         self.crate_position = crate_position
#         self.man_position = man_position
#         self.last_move = last_move
#         self.current_moves = current_moves


class State:

    def __init__(self, crate_position, man_position, wall_position, crate_destination):
        self.crate_position = crate_position
        self.man_position = man_position
        self.crate_destination = crate_destination
        self.wall_position = wall_position

    def move(self,direction):
        pass
        # self.man_position


# class FinalState:
#
#     def __init__(self, man_position, wall_position, crate_destination):
#         self.crate_position = crate_destination
#         self.man_position = man_position,
#         self.crate_destination = crate_destination
#         self.wall_position = wall_position
