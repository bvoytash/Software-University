def reduce_symbol_t(matrix,row, col, counter, player_1_score, player_2_score):
    sum_row = int(matrix[0][col]) + int(matrix[-1][col])
    sum_col = int(matrix[row][0]) + int(matrix[row][-1])
    total_sum = 3 * (sum_col + sum_row)
    if counter % 2 == 0:
        player_2_score -= total_sum
    else:
        player_1_score -= total_sum
    return player_1_score, player_2_score

def reduce_symbol_d(matrix, row, col, counter, player_1_score, player_2_score):
    sum_row = int(matrix[0][col]) + int(matrix[-1][col])
    sum_col = int(matrix[row][0]) + int(matrix[row][-1])
    total_sum = 2 * (sum_col + sum_row)
    if counter % 2 == 0:
        player_2_score -= total_sum
    else:
        player_1_score -= total_sum
    return player_1_score, player_2_score

def reduce_points(counter, points, player_1_score, player_2_score):
    if counter % 2 == 0:
        player_2_score -= points
    else:
        player_1_score -= points
    return player_1_score, player_2_score

def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        return True
    return False

player_1, player_2 = input().split(", ")
matrix = []
for i in range(1, 8):
    current_row = [el for el in input().split()]
    matrix.append(current_row)

player_1_score = 501
player_2_score = 501
p1_throw = 0
p2_throw = 0
counter = 1

while player_1_score > 0 and player_2_score > 0:
    command = input()
    command = command[1:-1]
    row = int(command.split(", ")[0])
    col = int(command.split(", ")[1])

    if is_valid(matrix, row, col):

        if matrix[row][col].isdigit():
            points = int(matrix[row][col])
            player_1_score, player_2_score = reduce_points(counter, points, player_1_score, player_2_score)
        elif matrix[row][col] == "D":
            player_1_score, player_2_score = reduce_symbol_d(matrix,row, col, counter, player_1_score, player_2_score)
        elif matrix[row][col] == "T":
            player_1_score, player_2_score = reduce_symbol_t(matrix,row, col, counter, player_1_score, player_2_score)
        elif matrix[row][col] == "B":
            if counter == 2:
                player_2_score = 0
                p2_throw += 1
            else:
                player_1_score = 0
                p1_throw += 1
            break

    else:
        if counter == 2:
            p2_throw += 1
            counter -= 1
        else:
            counter += 1
            p1_throw += 1
        continue

    if counter == 2:
        p2_throw += 1
        counter -= 1
    else:
        p1_throw += 1
        counter += 1

if player_1_score <= 0:
    print(f"{player_1} won the game with {p1_throw} throws!")
if player_2_score <= 0:
    print(f"{player_2} won the game with {p2_throw} throws!")


