def read_matrix():
    row, col = map(int, input().split())
    matrix = []
    for row_index in range(row):
        current_col = input().split()
        matrix.append(current_col)
    return matrix

def find_the_square(matrix, row, col):
     current = matrix[row][col]
     next_to_current = matrix[row][col + 1]
     bottom = matrix[row + 1][col]
     next_to_bottom = matrix[row+1][col+1]
     if current == next_to_current and current == bottom and current == next_to_bottom:
        return True
     return False


counter = 0
matrix = read_matrix()

for row_index in range(len(matrix) - 1):
    for col_index in range(len(matrix[0]) - 1):
        if find_the_square(matrix, row_index, col_index):
            counter += 1
print(counter)

