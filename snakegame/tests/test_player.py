#!/usr/bin/env python
# test_player.py

import unittest

from snakegame.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.p = Player("Bob")

    def test_player(self):
        self.assertEqual(self.p.player_name, "Bob")
        self.assertEqual(self.p.score, 0)

    def test_add_point(self):
        self.p.add_point()
        self.assertEqual(self.p.score, 1)

    def test_load_high_score(self):
        self.assertTrue(self.p.load_high_score())
        self.assertNotEqual(self.p.high_score_player, "Unknown")
        self.assertNotEqual(self.p.high_score, 0)

    def test_save_high_score(self):
        self.p.load_high_score()
        self.assertTrue(self.p.save_high_score())

    def test_is_high_score(self):
        self.p.load_high_score()

        tmp_high_score_player = self.p.high_score_player
        tmp_high_score = self.p.high_score
        self.p.score = 5000

        self.assertTrue(self.p.is_high_score())

        self.p.high_score_player = tmp_high_score_player
        self.p.high_score = tmp_high_score

        self.p.save_high_score()

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
