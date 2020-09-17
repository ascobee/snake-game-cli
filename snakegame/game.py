# game.py

from .apple import Apple
from .player import Player
from .snake import Snake


class Game:

    def __init__(self, player, height=25, width=25):
        self.height = height
        self.width = width
        self.top_border = 0
        self.left_border = 0
        self.bottom_border = self.height - 1
        self.right_border = self.width - 1
        self.snake = Snake([[2, 4], [3, 4], [4, 4], [5, 4]])
        self.apple = Apple(self.height, self.width)
        self.player = player

    def build_board(self):
        board_matrix = [[' ' for i in range(self.width)]
                        for j in range(self.height)]

        for i, row in enumerate(board_matrix):
            if i == self.top_border or i == self.bottom_border:
                for j, val in enumerate(row):
                    board_matrix[self.top_border][j] = "-"
                    board_matrix[self.bottom_border][j] = "-"
            else:
                board_matrix[i][self.left_border] = "|"
                board_matrix[i][self.right_border] = "|"

        return board_matrix

    def print_board(self):
        board = self.build_board()

        self.snake.print_snake(board)

        self.apple.print_apple(board)

        for row in board:
            print(" ".join(map(str, row)))

    def move_snake(self, direction):
        self.snake.move(direction)

    def snake_eats_apple(self):
        head = self.snake.head()
        apple_position = self.apple.get_apple()

        if head == apple_position:
            self.apple.apple_is_set = False

            new_tail = self.snake.body[0]
            self.snake.body.insert(0, new_tail)

            self.player.add_point()

    def game_over(self):
        head = self.snake.head()

        if head in self.snake.body[:-1]:
            return True
        elif 0 in head:
            return True
        elif self.right_border in head:
            return True
        elif self.bottom_border in head:
            return True

        return False
