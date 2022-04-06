from project_1.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return  f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for i, player in enumerate(self.players):
            if player.name == player_name:
                self.players.pop(i)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'
        # if player_name in self.players:
        #     self.players.remove(player_name)
        #     player_name.guild = "Unaffiliated"
        #     return f"Player {player_name.name} has been removed from the guild."
        # else:
        #     return f"Player {player_name.name} is not in the guild."

    def guild_info(self):
        info = []
        info.append(f"Guild: {self.name}")
        for pl in self.players:
            info.append(pl.player_info())
        return "\n".join(info)



