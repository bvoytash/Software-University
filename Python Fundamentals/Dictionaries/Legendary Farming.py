command = input()
my_dict = {"Shadowmourne": ["shards", 0], "Valanyr": ["fragments", 0], "Dragonwrath": ["motes", 0]}
junk_items = {}
Flag = False
winner = None
while True:
    data = command.split()
    for el in range(0, len(data), 2):
        quantity = int(data[el])
        item = (data[el + 1]).lower()

        if item == "motes":
            my_dict["Dragonwrath"][1] += quantity
        elif item == "shards":
            my_dict["Shadowmourne"][1] += quantity
        elif item == "fragments":
            my_dict["Valanyr"][1] += quantity
        else:
            if not item in junk_items:
                junk_items[item] = quantity
            else:
                junk_items[item] += quantity

        for key, value in my_dict.items():
            if my_dict[key]:
                if my_dict[key][1] >= 250:
                    winner = key
                    my_dict[key][1] -= 250
                    Flag = True
                    break
        if Flag:
            break
    if Flag:
        break
    command = input()

print(f"{winner} obtained!")
rest_items = {}
for key, value in my_dict.items():
    rest_items[value[0]] = value[1]

sorted_dict = dict(sorted(rest_items.items(), key= lambda x : (-x[1], x[0])))
for key, value in sorted_dict.items():
    print(f"{key}: {value}")

sorted_rest = dict(sorted(junk_items.items(), key= lambda x: x[0]))
for key, value in sorted_rest.items():
    print(f"{key}: {value}")


