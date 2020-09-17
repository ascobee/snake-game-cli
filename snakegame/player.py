# player.py


class Player:

    def __init__(self):
        self.player = "player1"
        self.score = 0
        self.high_score_player = "Unknown"
        self.high_score = 0

    def set_player_name(self, player):
        self.player = player

    def get_player_name(self):
        return self.player

    def get_player_score(self):
        return self.score

    def set_high_score_name(self, high_score_player):
        self.high_score_player = high_score_player

    def get_high_score_name(self):
        return self.high_score_player

    def set_high_score(self, high_score):
        self.high_score = high_score

    def get_high_score(self):
        return self.high_score

    def add_point(self):
        self.score += 1

    def save_high_score(self):
        high_score_list = [self.high_score_player, "\n", str(self.high_score)]
        f = open("../snakegame-git/data/highscore.txt", "w")
        f.writelines(high_score_list)
        f.close()
        print("New high score saved to file!")

    def load_high_score(self):
        with open("../snakegame-git/data/highscore.txt", "r") as f:
            self.set_high_score_name(f.readline().strip("\n"))
            self.set_high_score(int(f.readline()))

    def validate_player(self, msg):
        while True:
            try:
                name = input(msg)
                if name.isalpha():
                    return self.set_player_name(name.upper())

            except IndexError as err:
                continue
