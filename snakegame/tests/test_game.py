# test_game.py

import unittest

from snakegame.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game("Bob", 10, 10)

    def test_build_board(self):
        board = self.g.build_board()

        self.assertEqual(len(board), 10)
        self.assertEqual(len(board[0]), 10)

    def test_print_board(self):
        pass

    def test_snake_eats_apple(self):
        pass

    def test_is_game_over(self):
        lst = [
            self.g.snake.body[0],
            [0, 1],
            [1, 0],
            [1, self.g.right_border],
            [self.g.bottom_border, 1]
        ]

        for pos in lst:
            self.g.snake.body[-1] = pos
            self.assertTrue(self.g.is_game_over())

    # def test_is_game_over(self):
        # is_game_over = self.g.is_game_over

        # self.g.snake.body[-1] = self.g.snake.body[0]
        # self.assertTrue(is_game_over())

        # self.g.snake.body[-1] = [0, 1]
        # self.assertTrue(is_game_over())

        # self.g.snake.body[-1] = [1, self.g.right_border]
        # self.assertTrue(is_game_over())

        # self.g.snake.body[-1] = [self.g.bottom_border, 1]
        # self.assertTrue(is_game_over())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
