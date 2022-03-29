working_day_events = input().split("|")

current_energy = 100
current_coins = 100
Flag = False

for el in working_day_events:
    arg = el.split("-")
    event = arg[0]
    amount = int(arg[1])

    if event == "rest":
        gained_energy = 0
        if current_energy + amount <= 100:
            current_energy += amount
            gained_energy = amount
        else:
            gained_energy = 100 - current_energy
            current_energy = 100

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event == "order":

        if current_energy - 30 >= 0:
            current_energy -= 30
            current_coins += amount
            print(f"You earned {amount} coins.")
        else:
            current_energy += 50
            print("You had to rest!")

    else:
        if current_coins - amount > 0:
            current_coins -= amount
            print(f"You bought {event}.")
        else:
            Flag = True
            print(f"Closed! Cannot afford {event}.")
            break

if not Flag:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
