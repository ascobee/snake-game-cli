# app.py


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
    player1 = Player()
    game = Game(player1)

    if active_player:
        player1.set_player_name(active_player)
    else:
        player1.validate_player("Name your player: ")

    player_name = player1.get_player_name()

    player1.load_high_score()

    high_score_name = player1.get_high_score_name()
    high_score = player1.get_high_score()

    while True:
        player_score = player1.get_player_score()

        update_screen(game, high_score_name, high_score,
                      player_name, player_score)

        command = timeout_input(
            0.5, "Direction: ", last_move)

        new_direction = keyboard_commands(command)

        if new_direction == "QUIT":
            goodbye_msg(player_name)
            continue_playing = False
            break
        elif not new_direction:
            continue

        last_move = command

        game.move_snake(new_direction)
        game.snake_eats_apple()

        if game.game_over():
            update_screen(game, high_score_name, high_score,
                          player_name, player_score)
            print("\nGAME OVER!")
            break

    if player_score > high_score:
        player1.set_high_score(player_score)
        player1.set_high_score_name(player_name)

        high_score_name = player1.get_high_score_name()
        high_score = player1.get_high_score()

        player1.save_high_score()

        update_screen(game, high_score_name, high_score,
                      player_name, player_score)
        print(
            player_name,
            ", YOU HAVE THE NEW HIGH SCORE! : ",
            player_score,
            sep=''
        )

    if continue_playing:
        return play_again(player_name)


def play_again(name):
    while True:
        response = validate_player_input("Play Again? (Y/N): ")

        if response == "Y":
            return play_game(name)
        elif response == "N":
            return goodbye_msg(name)


def validate_player_input(msg):
    while True:
        try:
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


def scoreboard(high_score_name, high_score, player_name, player_score):
    print(
        "\nHIGH SCORE ({}): {}".format(high_score_name, high_score),
        "{}'s SCORE: {}\n".format(player_name, player_score),
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


def update_screen(game, high_score_name, high_score, player_name, player_score):
    clear_screen()
    menu()
    scoreboard(high_score_name, high_score,
               player_name, player_score)
    game.print_board()


def goodbye_msg(name):
    print(
        "\nThanks for playing, {}!".format(name),
        "\nQuitting program...",
        sep='\n'
    )


if __name__ == "__main__":
    play_game()
