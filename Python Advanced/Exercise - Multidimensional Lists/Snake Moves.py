from collections import deque

def read_matrix():
    row, col = map(int, input().split())
    matrix = []
    for row_index in range(row):
        current_row = []
        for col_index in range(col):
            current_row.append("")
        matrix.append(current_row)
    return matrix

matrix = read_matrix()
text = deque(input())

for r in range(len(matrix)):
    for c in range (len(matrix[0])):
        if  r % 2 == 0:
            current_el = text.popleft()
            matrix[r][c] = current_el
            text.append(current_el)
        else:
            col = len(matrix[0]) - c - 1
            current_el = text.popleft()
            matrix[r][col] = current_el
            text.append(current_el)

for row in matrix:
    print(''.join(map(str, row)))





