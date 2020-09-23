# test_app.py


import unittest
from unittest.mock import patch

from snakegame import app
from snakegame.player import Player


class TestApp(unittest.TestCase):

    def setUp(self):
        self.name = "Bob"
        self.score = 0
        self.high_score_name = "John"
        self.high_score = 50
        self.player = Player("Bob")
        self.player.high_score_player = self.high_score_name
        self.player.high_score = self.high_score

    def test_play_game(self):
        pass

    def test_play_again(self):
        pass
    #     with patch('builtins.print') as mock_print:
    #         with patch('builtins.input', return_value='N') as mock_input:
    #             play_again("Bob")

    #             mock_input.assert_called_once()
    #             mock_print.assert_called_once_with(
    #                 "\nThanks for playing, Bob!\n\nQuitting program...")

    #     with patch('builtins.input', return_value='Y') as mock_input:
    #         self.assertEqual(play_again("Bob"), play_game("Bob"), "IDK")

    #         mock_input.assert_called_once()

    def test_validate_player_input(self):
        pass

    def test_timeout_input(self):
        pass

    def test_menu(self):
        with patch('builtins.print') as mock_print:
            app.menu()
            mock_print.assert_called_once_with(
                "****** SNAKE ******\n",
                "Navigation Keys:",
                "E - UP",
                "D - DOWN",
                "S - LEFT",
                "F - RIGHT",
                "Q - QUIT",
                sep='\n'
            )

    def test_scoreboard(self):
        with patch('builtins.print') as mock_print:
            app.scoreboard(self.player)
            mock_print.assert_called_once_with(
                f"\nHIGH SCORE ({self.high_score_name}): {self.high_score}",
                f"{self.name}'S SCORE: {self.score}\n",
                sep='\n'
            )

    def test_keyboard_commands(self):
        self.assertEqual(app.keyboard_commands("E"), [-1, 0])
        self.assertEqual(app.keyboard_commands("D"), [1, 0])
        self.assertEqual(app.keyboard_commands("S"), [0, -1])
        self.assertEqual(app.keyboard_commands("F"), [0, 1])
        self.assertEqual(app.keyboard_commands("Q"), "QUIT")
        self.assertEqual(app.keyboard_commands("K"), None)

    def test_clear_screen(self):
        pass

    def test_update_screen(self):
        pass

    def test_goodbye_msg(self):
        with patch('builtins.print') as mock_print:
            app.goodbye_msg(self.player.player_name)
            mock_print.assert_called_once_with(
                f"\nThanks for playing, {self.name}!\n\nQuitting program..."
            )

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
