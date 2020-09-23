# main.py


import select
import sys
from os import name, system

from .game import Game
from .player import Player


UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]


def play_game(active_player=None):
    continue_playing = True
    last_move = "D"

    if not active_player:
        active_player = validate_player_input("Name your player: ", True)

    player1 = Player(active_player)

    game = Game(player1)

    player1.load_high_score()

    while True:
        update_screen(game, player1)

        command = timeout_input(
            0.5, "Direction: ", last_move)

        new_direction = keyboard_commands(command)

        if new_direction == "QUIT":
            goodbye_msg(player1.player_name)
            continue_playing = False
            break
        elif not new_direction:
            continue

        last_move = command

        game.snake.move(new_direction)
        game.snake_eats_apple()

        if game.is_game_over():
            update_screen(game, player1)
            print("\nGAME OVER!")
            break

    if player1.is_high_score():
        update_screen(game, player1)
        print(f"{player1.player_name}, YOU HAVE THE NEW HIGH SCORE! : {player1.score}")

    if continue_playing:
        return play_again(player1.player_name)


def play_again(player_name):
    while True:
        response = validate_player_input("Play Again? (Y/N): ")

        if response == "Y":
            return play_game(player_name)
        elif response == "N":
            return goodbye_msg(player_name)


def validate_player_input(msg, is_name=False):
    while True:
        try:
            if is_name:
                command = input(msg)
            else:
                command = input(msg)[0]

            if command.isalpha():
                return command.upper()

        except IndexError as err:
            continue


def timeout_input(timeout, prompt="", timeout_value=None):
    while True:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            command = sys.stdin.readline(1).rstrip('\n')
            if command.isalpha():
                return command.upper()
        else:
            sys.stdout.write('\n')
            sys.stdout.flush()
            return timeout_value


def menu():
    print(
        "****** SNAKE ******\n",
        "Navigation Keys:",
        "E - UP",
        "D - DOWN",
        "S - LEFT",
        "F - RIGHT",
        "Q - QUIT",
        sep='\n'
    )


def scoreboard(player):
    print(
        f"\nHIGH SCORE ({player.high_score_player}): {player.high_score}",
        f"{player.player_name}'S SCORE: {player.score}\n",
        sep='\n'
    )


def keyboard_commands(key_commands):
    switcher = {
        "E": UP,
        "D": DOWN,
        "S": LEFT,
        "F": RIGHT,
        "Q": "QUIT"
    }
    return switcher.get(key_commands, None)


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def update_screen(game, player):
    clear_screen()
    menu()
    scoreboard(player)
    game.print_board()


def goodbye_msg(player_name):
    print(f"\nThanks for playing, {player_name}!\n\nQuitting program...")


if __name__ == "__main__":
    play_game()
