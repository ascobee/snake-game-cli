#!/usr/bin/env python
# test_apple.py

import unittest

from snakegame.apple import Apple


class TestApple(unittest.TestCase):

    def setUp(self):
        self.a = Apple(10, 10)

    def test_move(self):
        self.assertIn(self.a.row, range(1, 9))
        self.assertIn(self.a.col, range(1, 9))

    def test_print_apple(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
