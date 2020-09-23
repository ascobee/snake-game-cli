#!/usr/bin/env python
# test_snake.py

import unittest

from snakegame.snake import Snake
from snakegame.game import Game


UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.body_initial = [[2, 4], [3, 4], [4, 4], [5, 4]]
        self.game = Game("Bob", 10, 10)
        self.s = Snake(self.body_initial)

    def test_move(self):
        directions = [RIGHT, UP, LEFT, DOWN]
        body_final = [[5, 5], [4, 5], [4, 4], [5, 4]]

        for direction in directions:
            self.s.move(direction)

        self.assertEqual(self.s.body, body_final)

    def test_head(self):
        self.assertEqual(self.s.head(), [5, 4])

    def test_print_snake(self):
        board = self.game.build_board()
        head = self.body_initial[-1]

        self.s.print_snake(board)

        for pos in self.body_initial[:-1]:
            self.assertEqual(board[pos[0]][pos[1]], "O")

        self.assertEqual(board[head[0]][head[1]], "X")

    def test_grow(self):
        body_grow = [[2, 4], [2, 4], [3, 4], [4, 4], [5, 4]]

        self.s.grow()

        self.assertEqual(self.s.body, body_grow)

    def tearDown(self):
        self.body_initial = []


if __name__ == "__main__":
    unittest.main()
