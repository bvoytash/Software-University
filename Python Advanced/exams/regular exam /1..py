from collections import deque
chocolates = [int(el) for el in input().split(", ")]
milk = deque([int(el) for el in input().split(", ")])

shakers = 0

while chocolates and milk:
    current_chocolate = chocolates[-1]
    current_milk = milk[0]
    if current_chocolate <= 0:
        chocolates.pop()
        continue
    if current_milk <= 0:
        milk.popleft()
        continue

    if current_chocolate == current_milk:
        shakers += 1
        chocolates.pop()
        milk.popleft()
        if shakers >= 5:
            break
    else:
        milk.append(current_milk)
        milk.popleft()
        chocolates[-1] -= 5

if shakers >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    chocolates = [str(el) for el in chocolates]
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")

if milk:
    milk = [str(el) for el in milk]
    print(f"Milk: {', '.join(milk)}")
else:
    print("Milk: empty")