neighborhood = [int(el) for el in input().split("@")]

command = input()
start_index = 0
Flag = True
while not command == "Love!":

    jump = int(command.split()[1])

    if not jump + start_index >= len(neighborhood):
        if neighborhood[(jump + start_index)] >= 2:
            neighborhood[(jump + start_index)] -= 2
            if neighborhood[(jump + start_index)] == 0:
                print(f"Place {jump + start_index} has Valentine's day." )

        else:
            print(f"Place {(jump + start_index)} already had Valentine's day.")
        Flag = True
    else:
        if neighborhood[0] >= 2:
            neighborhood[0] -= 2
            if neighborhood[0] <= 0:
                print(f"Place {0} has Valentine's day." )
        else:
            print(f"Place {0} already had Valentine's day.")
        start_index = 0
        Flag = False

    if Flag:
        start_index += jump

    command = input()

print(f"Cupid's last position was {start_index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    count = 0
    for el in neighborhood:
        if el != 0:
            count += 1
    print(f"Cupid has failed {count} places.")
