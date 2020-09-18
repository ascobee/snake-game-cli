# player.py


class Player:

    def __init__(self, player="player1"):
        self.player = player
        self.score = 0
        self.high_score_player = "Unknown"
        self.high_score = 0

    def add_point(self):
        self.score += 1

    def is_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_player = self.player
            self.save_high_score()
            return True
        return False

    def save_high_score(self):
        f = open("../snakegame-git/data/highscore.txt", "w")
        f.writelines([self.high_score_player, "\n", str(self.high_score)])
        f.close()
        print("New high score saved to file!")

    def load_high_score(self):
        with open("../snakegame-git/data/highscore.txt", "r") as f:
            self.high_score_player = f.readline().strip("\n")
            self.high_score = int(f.readline())
