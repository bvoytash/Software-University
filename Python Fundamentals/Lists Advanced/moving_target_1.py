line = [int(el) for el in input().split()]

command = input()

while not command == "End":
    action = command.split()[0]
    if action == "Shoot":
        index = int(command.split()[1])
        power = int(command.split()[2])
        if index < len(line) and line[index] > 0:
            line[index] -= power
            if line[index] <= 0:
                line.pop(index)

    elif action == "Add":
        index = int(command.split()[1])
        value = int(command.split()[2])
        if index < len(line):
            line.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(command.split()[1])
        radius = int(command.split()[2])
       #TODO

        else:
            print("Strike missed!")
    command = input()
line = [str(el) for el in line]
print("|".join(line))



