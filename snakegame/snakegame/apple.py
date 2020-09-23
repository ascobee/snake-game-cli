# apple.py

from random import randint


class Apple:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.move()

    def move(self):
        self.col = randint(1, self.width - 2)
        self.row = randint(1, self.height - 2)

    def print_apple(self, board):
        board[self.row][self.col] = "*"
