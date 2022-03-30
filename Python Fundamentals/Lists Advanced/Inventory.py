inventory = input().split(", ")
command = input()


while not command == "Craft!":
    action = command.split(" - ")[0]

    if action == "Collect":
        item = command.split(" - ")[1]
        if item not in inventory:
            inventory.append(item)

    if action == "Drop":
        item = command.split(" - ")[1]
        if item in inventory:
            inventory.remove(item)

    if action == "Combine Items":
        item = command.split(" - ")[1]
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)

    if action == "Renew":
        item = command.split(" - ")[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()
print(", ".join(inventory))