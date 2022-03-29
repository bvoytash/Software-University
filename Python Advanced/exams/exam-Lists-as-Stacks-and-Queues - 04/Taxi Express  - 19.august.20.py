from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxi = [int(el) for el in input().split(", ")]

total_time = 0
while customers and taxi:
    if customers[0] <= taxi[-1]:
        total_time += customers.popleft()
        taxi.pop()
    else:
        taxi.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")




