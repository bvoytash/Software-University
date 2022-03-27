def read_matrix():
    row = int(input())
    matrix = []
    for _ in range(row):
        current_row = list(map(int, input().split()))
        matrix.append(current_row)
    return matrix

def explode(matrix, row, col):
    bomb = matrix[row][col]
    for r in range(row-1, row+1 + 1):
        for c in range(col-1, col+1 + 1):
            if is_valid(matrix, r, c) and matrix[r][c] > 0:
                a = [r, c]
                if a in bombs_coordinates:
                    matrix[r][c] -= bomb
                    # if matrix[r][c] < 0:
                        # matrix[r][c] = 0
                else:
                    matrix[r][c] -= bomb

def is_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        return True
    return False


matrix = read_matrix()
data = input().split()
bombs_coordinates = []
for el in data:
    coordinates = list(map(int, el.split(",")))
    bombs_coordinates.append(coordinates)

for bomb in bombs_coordinates:
    r = bomb[0]
    c = bomb[1]
    if matrix[r][c] > 0:
        explode(matrix, r, c)

alive = 0
total_sum = []
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] > 0:
            alive += 1
            total_sum.append(matrix[r][c])
print(f"Alive cells: {alive}")
print(f"Sum: {sum(total_sum)}")
for rows in matrix:
    current_row = list(map(str, rows))
    print(' '.join(current_row))


