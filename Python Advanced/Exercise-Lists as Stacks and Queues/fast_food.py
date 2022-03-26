from collections import deque
food = int(input())
orders = [int(el) for el in input().split()]
orders = deque(orders)

the_biggest = max(orders)

while food > 0:
    if orders and food >= orders[0]:
        food -= orders.popleft()
    else:
        break

print(the_biggest)
if not orders:
    print("Orders complete")
else:
    orders = [str(el) for el in orders]
    print(f"Orders left: {' '.join(orders)}")

