from math import floor
def next_position(player_position, command):
    row = player_position[0]
    col = player_position[1]
    if command == "up":
       row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1
    return row, col

def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False

n = int(input())
player_position = []
matrix = []
for i in range(n):
    current_row = input().split()
    matrix.append(current_row)
    if "P" in current_row:
        player_position = [i, current_row.index("P")]
possible_dir = ["up", "down", "left", "right"]
position_with_coins = []
coins = 0
Lose = False
Win = False
command = input()
while command:
    if not command in possible_dir:
        continue
    next_row, next_col = next_position(player_position, command)
    if is_valid(matrix, next_row, next_col) and matrix[next_row][next_col] != "X":
        current_coins = int(matrix[next_row][next_col])
        coins += current_coins
        player_position = [next_row, next_col]
        position_with_coins.append(player_position)
        matrix[next_row][next_col] = "P"
    else:
        coins = coins / 2
        Lose = True
        break

    if coins >= 100:
        Win = True
        break
    command = input()

coins = floor(coins)
if Win:
    print(f"You won! You've collected {coins} coins.")
    print("Your path:")
    for i in position_with_coins:
        print(i)
else:
    print(f"Game over! You've collected {coins} coins.")
    print("Your path:")
    for i in position_with_coins:
        print(i)