def move_bunnies(matrix, bunnies_positions):
    for b in bunnies_positions:
        r = b[0]
        c = b[1]
        if is_valid(matrix, r-1, c):
            matrix[r-1][c] = "B"
        if is_valid(matrix, r+1, c):
            matrix[r + 1][c] = "B"
        if is_valid(matrix, r, c+1):
            matrix[r][c + 1] = "B"
        if is_valid(matrix, r, c-1):
            matrix[r][c - 1] = "B"

def move_player(player_position, dir):
    row = player_position[0]
    col = player_position[1]
    if dir == "U":
        row -= 1
    elif dir == "D":
        row += 1
    elif dir == "L":
        col -= 1
    elif dir == "R":
        col += 1
    return row, col


def find_bunnies(matrix):
    bunnies_positions = []
    for row in range (len(matrix)):
        for col in range (len(matrix[0])):
            if matrix[row][col] == "B":
                bunnies_positions.append([row, col])
    return bunnies_positions


def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        return True
    return False

rows, cols = (map(int, input().split()))
matrix = []
player_position = []
for r in range(rows):
    current_row = [el for el in input()]
    matrix.append(current_row)
    if "P" in current_row:
        player_position = [r, current_row.index("P")]

last_position = []
direction_of_player = [el for el in input()]
WIN = False
LOSE = False

for dir in direction_of_player:
    next_player_position = move_player(player_position, dir)
    if is_valid(matrix, next_player_position[0], next_player_position[1]):

        if matrix[next_player_position[0]][next_player_position[1]] == ".":
            matrix[next_player_position[0]][next_player_position[1]] = "P"
            matrix[player_position[0]][player_position[1]] = "."
            player_position = [next_player_position[0], next_player_position[1]]
        else:
            LOSE = True
            last_position = [next_player_position[0], next_player_position[1]]

    else:
        WIN = True
        matrix[player_position[0]][player_position[1]] = "."
        last_position = [player_position[0], player_position[1]]

    bunnies_positions = find_bunnies(matrix)
    move_bunnies(matrix, bunnies_positions)
    if WIN:
        break

    Flag = False
    for rows in matrix:
        if "P" in rows:
            Flag = True
    if not Flag:
        LOSE = True
        last_position = [next_player_position[0], next_player_position[1]]
        break

[print(*line, sep="") for line in matrix]

if WIN:
    print(f"won: {last_position[0]} {last_position[1]}")
else:
    print(f"dead: {last_position[0]} {last_position[1]}")




