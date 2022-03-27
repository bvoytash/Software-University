def read_matrix():
    row, col = map(int, input().split())
    matrix = []
    for row_index in range(row):
        current_row = input().split()
        matrix.append(current_row)
    return matrix

matrix = read_matrix()

command = input()
while not command == "END":

    if command.split()[0] != "swap" or len(command.split()) != 5:
        print("Invalid input!")
        command = input()
        continue
    for el in command.split()[1:]:
        if not el.isdigit():
            print("Invalid input!")
            command = input()
            continue

    if command.split()[0] == "swap":
        command = command.split()
        command.pop(0)
        first_coordinate = list(map(int, command[:2]))
        second_coordinate = list(map(int, command[2:]))

        if len(matrix) < first_coordinate[0] or len(matrix) < second_coordinate[0] or len(matrix[0]) < first_coordinate[1]\
                or len(matrix[0]) < second_coordinate[1]:
            print("Invalid input!")
            command = input()
            continue

        matrix[first_coordinate[0]][first_coordinate[1]], matrix[second_coordinate[0]][second_coordinate[1]]\
            = matrix[second_coordinate[0]][second_coordinate[1]], matrix[first_coordinate[0]][first_coordinate[1]]
        for rows in matrix:
            print(' '.join(map(str, rows)))

    command = input()