def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False

matrix = []
player_position = []
targets = 0
hit_targets = 0
targets_indx = []
for rows in range(5):
    current_row = [el for el in input().split()]
    matrix.append(current_row)
    if "A" in current_row:
        player_position.append(rows)
        player_position.append(current_row.index("A"))
    for el in current_row:
        if el == "x":
            targets += 1

dirs = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

count_of_commands = int(input())
for i in range(count_of_commands):
    command = input().split()
    action = command[0]
    dir = command[1]

    if action == "move":
        steps = int(command[2])
        final_row = player_position[0] + dirs[dir][0] * steps
        final_col = player_position[1] + dirs[dir][1] * steps
        if is_valid(matrix, final_row, final_col) and matrix[final_row][final_col] == ".":
            matrix[player_position[0]][player_position[1]] = "."
            player_position = [final_row, final_col]
            matrix[final_row][final_col] = "A"
            # for step in range(steps):
            #     next_row = player_position[0] + dirs[dir][0]
            #     next_col = player_position[1] + dirs[dir][1]
            #     if matrix[next_row][next_col] == ".":
            #         matrix[player_position[0]][player_position[1]] = "."
            #         player_position = [next_row, next_col]
            #         matrix[next_row][next_col] = "A"
            #     elif matrix[next_row][next_col] == "x":
            #         matrix[player_position[0]][player_position[1]] = "."
            #         player_position = [next_row, next_col]

    elif action == "shoot":
        target_row = player_position[0]
        target_col = player_position[1]
        for i in range(len(matrix)):
            target_row += dirs[dir][0]
            target_col += dirs[dir][1]
            if is_valid(matrix, target_row, target_col):
                if matrix[target_row][target_col] == "x":
                    hit_targets += 1
                    matrix[target_row][target_col] = "."
                    targets_indx.append([target_row, target_col])
                    break

        if targets == hit_targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets > hit_targets:
    lefts = targets - hit_targets
    print(f"Training not completed! {lefts} targets left.")

for el in targets_indx:
    print(el)






