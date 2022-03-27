def read_matrix():
    row, col = map(int, input().split())
    matrix = []
    for row_index in range(row):
        current_row = list(map(int, input().split()))
        matrix.append(current_row)
    return matrix


def sub_matrix_sum(matrix, row, col, size):
    sum_sub_matrix = 0
    for row_index in range(row, row+size):
        for col_index in range(col, col+size):
            sum_sub_matrix += matrix[row_index][col_index]
    return sum_sub_matrix


def find_biggest(matrix, size):
    the_biggest = sub_matrix_sum(matrix, 0, 0, size)
    coordinates = [0, 0]
    for row_index in range(len(matrix) - size + 1):
        for col_index in range(len(matrix[0]) - size + 1):
            current_sum = sub_matrix_sum(matrix, row_index, col_index, size)
            if current_sum > the_biggest:
                the_biggest = current_sum
                coordinates[0] = row_index
                coordinates[1] = col_index
    return coordinates

matrix = read_matrix()
size = 3

sub_matrix = []
sum_sub_matrix = 0
row, col = map(int, find_biggest(matrix,size))
for row_index in range(row, row + size):
    current_row = []
    for col_index in range(col, col + size):
        sum_sub_matrix += matrix[row_index][col_index]
        current_row.append(matrix[row_index][col_index])
    sub_matrix.append(current_row)
print(f"Sum = {sum_sub_matrix}")
for el in sub_matrix:
    print(' '.join(map(str, el)))