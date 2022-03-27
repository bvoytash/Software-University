def read_matrix():
    row = int(input())
    matrix = []
    for row_index in range(row):
        current = list(map(int, input().split()))
        matrix.append(current)
    return matrix

def primary_diagonal(matrix):
    p_diagonal = []
    for row_index in range(len(matrix)):
        p_diagonal.append(matrix[row_index][row_index])
    return p_diagonal

def secondary_diagonal(matrix):
    s_diagonal = []
    for row in range(len(matrix)):
        s_diagonal.append(matrix[row][(len(matrix) - 1) - row])
    return s_diagonal

def print_result(matrix):
    p = sum(primary_diagonal(matrix))
    s = sum(secondary_diagonal(matrix))
    diff = abs(p - s)
    print(diff)

matrix = read_matrix()
print_result(matrix)