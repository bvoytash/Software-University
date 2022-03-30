neighborhood = [int(el) for el in input().split("@")]

command = input()
jump = 0
while not command == "Love!":
    index = int(command.split()[1])
    jump += index
    if jump >= len(neighborhood):
        jump = 0
    if neighborhood[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        neighborhood[jump] -= 2
        if neighborhood[jump] == 0:
            print(f"Place {jump} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {jump}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    count = len([el for el in neighborhood if el > 0])
    print(f"Cupid has failed {count} places.")