items = input().split("|")
budget = float(input())

spend_money = 0
profit_list = []

for elements in items:
    type_item, price = elements.split("->")
    price = float(price)
    if price <= budget:

        if type_item == "Clothes" and price <= 50:
            budget -= price
            spend_money += price
            profit = (0.4 * price) + price
            profit_list.append(profit)
        elif type_item == "Shoes" and price <= 35:
            budget -= price
            spend_money += price
            profit = (0.4 * price) + price
            profit_list.append(profit)
        elif type_item == "Accessories" and price <= 20.50:
            budget -= price
            spend_money += price
            profit = (0.4 * price) + price
            profit_list.append(profit)

    else:
        continue

earn_money = 0
for nums in profit_list:
    earn_money += nums
    print(f"{nums:.2f}", end=" ")
print( )

total_profit = spend_money * 0.4
print(f"Profit: {total_profit:.2f}")

if (budget + earn_money) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")