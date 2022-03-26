n = 0
command = input()
phone_dict = {}
while True:
    if command.isdigit():
        n = int(command)
        break
    name, number = command.split("-")
    if not name in phone_dict:
        phone_dict[name] = number
    else:
        phone_dict[name] = number
    command = input()

for i in range(0, n):
    name = input()
    if name in phone_dict:
        print(f"{name} -> {phone_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")