targets = [int(el) for el in input().split()]
command = input()


while not command == "End":
    type = command.split()[0]
    index = int(command.split()[1])
    value = int(command.split()[2])

    if type == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif type == "Add":
        if 0 <= index < len(targets):
           targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif type == "Strike":
        if (index + value) < len(targets) and (index - value) >= 0:
            del targets[(index - value):((index + 1) + value)]
        else:
            print("Strike missed!")

    command = input()

str_list = [str(el) for el in targets]
final_string = "|".join(str_list)
print(final_string)

