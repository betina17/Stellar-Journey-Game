from src.controller.game_logistics import GameLogistics
from src.domain.domain import Board

import unittest


class TestPlaceStars(unittest.TestCase):

    def test_place_stars(self):
        game_board = Board()
        player_board = Board()
        game_logs = GameLogistics(game_board, player_board)
        game_board.new_star([3,4])
        self.assertTrue(self, game_logs.check_star_placement(3,5))
        self.assertTrue(self, game_logs.check_star_placement(2, 6))
        self.assertTrue(self, game_logs.check_star_placement(1,5))



if __name__ == '__main__':
    unittest.main()

