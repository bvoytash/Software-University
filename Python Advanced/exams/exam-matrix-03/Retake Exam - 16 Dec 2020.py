def move_player(r, c, command):
    if command == "down":
        r += 1
    elif command == "up":
        r -= 1
    elif command == "left":
        c -= 1
    elif command == "right":
        c += 1
    return r, c


def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False

word = input()
n = int(input())
matrix = []
player_position = []
for i in range(n):
    current_row = [el for el in input()]
    matrix.append(current_row)
    if "P" in current_row:
        player_position = [i, current_row.index("P")]

n_commands = int(input())
for i in range(n_commands):
    command = input()
    row, col = move_player(player_position[0], player_position[1], command)
    if is_valid(matrix, row, col):
        if matrix[row][col] == "-":
            matrix[row][col] = "P"
            matrix[player_position[0]][player_position[1]] = "-"
            player_position = [row, col]
        else:
            word += matrix[row][col]
            matrix[row][col] = "P"
            matrix[player_position[0]][player_position[1]] = "-"
            player_position = [row, col]

    else:
        word = word[:-1]

print(word)
for el in matrix:
    print(*el, sep="")




