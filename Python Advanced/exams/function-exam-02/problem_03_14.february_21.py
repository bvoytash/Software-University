def stock_availability(inventory, *args):
    action = args[0]

    if action == "delivery":
        boxes = args[1:]
        for el in boxes:
            inventory.append(el)

    elif action == "sell":
        rest = args[1:]
        if not rest:
            inventory.pop(0)
        elif str(rest[0]).isdigit():
            number = int(rest[0])
            for i in range(number):
                inventory.pop(0)
        else:
            # boxes = [el for el in rest]
            for el in rest:
                while el in inventory:
                    inventory.remove(el)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "cookie"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
