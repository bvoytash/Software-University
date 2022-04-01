n_commands = int(input())

parking = {}

for commands in range(0, n_commands):
    command = input().split()
    user = command[1]

    if command[0] == "register":
        number = command[2]
        if user not in parking:
            parking[user] = number
            print(f"{user} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")

    elif command[0] == "unregister":
        if not user in parking:
            print(f"ERROR: user {user} not found")
        else:
            parking.pop(user)
            print(f"{user} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")

