gifts = input().split()


while True:
    commands = input()

    if commands == "No Money":
        break

    if "OutOfStock" in commands:
        command, type_gift = commands.split()
        for el in gifts:
            if el == type_gift:
                index = gifts.index(el)
                gifts.remove(el)
                gifts.insert(index, "None")

    elif "Required" in commands:
        command, type_gift, index = commands.split()
        index = int(index)
        if len(gifts) - 1 >= index >= 0:
            gifts.pop(index)
            gifts.insert(index, type_gift)

    elif "JustInCase" in commands:
        command, type_gift = commands.split()
        gifts.pop(-1)
        gifts.append(type_gift)

for el in gifts:
    if not el == "None":
        print(el, end=" ")