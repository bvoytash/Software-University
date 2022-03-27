# def move(matrix, r, c, command):
#     current_position = []
#     if command == "up":
#         if is_valid(matrix, r, c):
#             current_position.append(r-1)
#             current_position.append(c)
#     elif command == "right":
#         if is_valid(matrix, r, c):
#             current_position.append(r)
#             current_position.append(c + 1)
#     elif command == "left":
#         if is_valid(matrix, r, c):
#             current_position.append(r)
#             current_position.append(c -1)
#     elif command == "down":
#         if is_valid(matrix, r, c):
#             current_position.append(r + 1)
#             current_position.append(c)
#     return current_position
#
# def is_valid(matrix, r, c):
#     if 0 <= r < len(matrix) and 0 <= c < len(matrix):
#         return True
#     return False
#
# rows = int(input())
# matrix =[]
# commands = input().split()
# for _ in range(rows):
#     current_row = input().split()
#     matrix.append(current_row)
#
# start_coordinate = []
# Flag = False
# for r in range(len(matrix)):
#     if Flag:
#         break
#     for c in range(len(matrix)):
#         if matrix[r][c] == "s":
#             start_coordinate.append(int(r))
#             start_coordinate.append(int(c))
#             Flag = True
#             break
# coals = 0
# r, c = start_coordinate
# a = None
# last_r = 0
# last_c = 0
# for command in commands:
#     current_position = move(matrix, r, c, command)
#     current_r = current_position[0]
#     current_c = current_position[1]
#     if not is_valid(matrix, current_r, current_c):
#         continue
#     if matrix[current_r][current_c] == "e":
#         print(f"Game over! ({current_r}, {current_c})")
#         a = 1
#         break
#     elif matrix[current_r][current_c] == "c":
#         coals += 1
#         matrix[current_r][current_c] = "*"
#         Flag = False
#         for row in matrix:
#             if "c" in row:
#                 Flag = True
#         if not Flag:
#             print(f"You collected all coals! ({current_r}, {current_c})")
#             a = 1
#             break
#     r, c = current_position
#     last_r = current_r
#     last_c = current_c
#
# coal_left = 0
# for r in range(len(matrix)):
#     for c in range(len(matrix)):
#         if matrix[r][c] == "c":
#             coal_left += 1
#
# if not a:
#     print(f"{coal_left} coals left. ({last_r}, {last_c})")

def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        return True
    return False

n = int(input())
directions = input().split()
matrix = []
player_position = []
coals_count = 0
collected_coals = 0
for i in range(n):
    current_row = input().split()
    matrix.append(current_row)
    if "s" in current_row:
        player_position.append(i)
        player_position.append(current_row.index("s"))
    for el in current_row:
        if el == "c":
            coals_count += 1

mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for dir in directions:
    next_row = player_position[0] + mapper[dir][0]
    next_col = player_position[1] + mapper[dir][1]
    if not is_valid(matrix, next_row, next_col):
        continue
    else:
        if matrix[next_row][next_col] == "*":
            matrix[player_position[0]][player_position[1]] = "*"
            player_position = [next_row, next_col]
            matrix[next_row][next_col] = "s"

        elif matrix[next_row][next_col] == "c":
            matrix[player_position[0]][player_position[1]] = "*"
            player_position = [next_row, next_col]
            matrix[next_row][next_col] = "s"
            collected_coals += 1
            if collected_coals == coals_count:
                print(f"You collected all coals! ({next_row}, {next_col})")
                exit()
        elif matrix[next_row][next_col] == "e":
            print(f"Game over! ({next_row}, {next_col})")
            exit()

if collected_coals < coals_count:
    remaining_coals = coals_count - collected_coals
    print(f"{remaining_coals} coals left. ({player_position[0]}, {player_position[1]})")
