
class OccupiedSpotException(RuntimeError):
    pass

class Board:

        UNOCCUPIED_SPOT = 0
        """Board is a matrix 3x3 when if all the elements are 0 then is ready to play"""
        def __init__(self):
            self._board = [[self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT],
                           [self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT],
                           [self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT, self.UNOCCUPIED_SPOT]]

        def is_empty(self):
            for i in self._board:
                for j in i:
                    if j != 0:
                        return False
            return True

        def player_do_a_moviment(self, player, x, y):
            self.validate_coordinates(x, y)

            if self._board[x][y] != self.UNOCCUPIED_SPOT:
                raise OccupiedSpotException("Oops, this spot is occupied")

            self._board[x][y] = player

        def free_spot(self, x, y):
            self.validate_coordinates(x, y)
            self._board[x][y] = self.UNOCCUPIED_SPOT

        def player_moves_piece(self, player, source_x, source_y, destiny_x, destiny_y):

            self.player_do_a_moviment(player, destiny_x, destiny_y)
            self.free_spot(source_x, source_y)

        def get_player_at_coordinate(self, x, y):
            """Get the player whihc occupies the coordinate"""
            self.validate_coordinates(x, y)

            return self._board[x][y]

        def validate_coordinates(self, x, y):
            if x > 2 or x < 0:
                raise RuntimeError("Wrong X coordination: ", x)
            if y > 2 or y < 0:
                raise RuntimeError("Wrong Y coordination: ", y)