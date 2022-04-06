from project.player.player import Player


class Advanced(Player):
    # HP = 250

    def __init__(self, username):
        super().__init__(username, 250)
