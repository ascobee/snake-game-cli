#!/usr/bin/env python
# snake.py


class Snake:

    def __init__(self, body):
        self.body = body

    def move(self, direction):
        self.direction = direction
        head = list(map(sum, zip(self.head(), self.direction)))
        self.body = self.body[1:] + [head]

    def head(self):
        return self.body[-1]

    def print_snake(self, board):
        for pos in self.body[:-1]:
            board[pos[0]][pos[1]] = "O"

        head = self.head()
        board[head[0]][head[1]] = "X"

    def grow(self):
        new_tail = self.body[0]
        self.body.insert(0, new_tail)
