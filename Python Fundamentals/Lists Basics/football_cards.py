cards = input()

my_list = []
removed_players = []
team_a = 11
team_b = 11

list_cards = cards.split()
for player in list_cards:
    if "A" in player and player not in removed_players:
        removed_players.append(player)
        team_a -= 1
    elif "B" in player and player not in removed_players:
        removed_players.append(player)
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if team_a < 7 or team_b < 7:
    print("Game was terminated")