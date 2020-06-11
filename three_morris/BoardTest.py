import unittest

from three_morris.Board import Board, OccupiedSpotException


class BoardTest(unittest.TestCase):
    player_1 = 1
    player_2 = 2
    def test_is_a_board_ready(self):
        board = Board()
        self.assertTrue(board.is_empty())

    def test_a_board_should_not_be_empty_after_a_valid_moviment(self):
        board = Board()
        board.player_do_a_moviment(self.player_1, 0, 0)

        self.assertFalse(board.is_empty())

    def test_invalid_x_coodinate_should_raise_an_expection(self):
        board = Board()

        with self.assertRaises(RuntimeError):
            board.player_do_a_moviment(self.player_1, -1, 0)

    def test_invalid_y_coodinate_should_raise_an_expection(self):
        board = Board()

        with self.assertRaises(RuntimeError):
            board.player_do_a_moviment(self.player_1, 1, -1)

    def test_occupied_coordinate(self):
        board = Board()
        board.player_do_a_moviment(self.player_1, 1, 1)

        with self.assertRaises(OccupiedSpotException):
            board.player_do_a_moviment(self.player_2, 1, 1)

    def test_player_can_move_from_0_0_to_1_1(self):
        board = Board()
        board.player_do_a_moviment(self.player_1, 0, 0)

        board.player_moves_piece(self.player_1, source_x=0, source_y=0, destiny_x=1, destiny_y=1)

        self.assertEquals(board.get_player_at_coordinate(1, 1), self.player_1)
