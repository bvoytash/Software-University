from project.player.player import Player


class Beginner(Player):
    # HP = 50

    def __init__(self, username):
        super().__init__(username, 50)
