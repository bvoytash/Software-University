def bomb_check(matrix, r, c):
    bombs = 0
    for row in range(r - 1, r + 2):
        for col in range(c -1, c + 2):
            if is_valid(matrix,row,col):
                if matrix[row][col] == "*":
                    bombs += 1
    return bombs

def is_valid(matrix, r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False

n = int(input())
bombs = int(input())

matrix = []
for r in range(n):
    matrix.append([])
    for col in range(n):
        matrix[r].append(".")

for _ in range(bombs):
    bomb_coordinate = [int(el) for el in input()[1:][:-1].split(", ")]
    row, col = bomb_coordinate
    matrix[row][col] = "*"

for r in range(n):
    for c in range(n):
        if not matrix[r][c] == "*":
            current_number = bomb_check(matrix, r, c)
            matrix[r][c] = current_number

for rows in matrix:
    print(*rows, sep=" ")
