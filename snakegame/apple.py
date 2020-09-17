# apple.py

from random import randint


class Apple:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.apple_is_set = False

    def set_apple(self):
        self.col = randint(1, self.width - 2)
        self.row = randint(1, self.height - 2)

    def get_apple(self):
        return [self.row, self.col]

    def print_apple(self, board):
        if not self.apple_is_set:
            self.set_apple()
            self.apple_is_set = True

        pos = self.get_apple()
        board[pos[0]][pos[1]] = "*"
