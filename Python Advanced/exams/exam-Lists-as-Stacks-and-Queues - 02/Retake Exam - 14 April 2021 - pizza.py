from collections import deque
pizza_orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]
total_pizza = 0
while pizza_orders and employees:
    current_order = pizza_orders[0]
    current_employee = employees[-1]

    if current_order <= 0:
        pizza_orders.popleft()
        continue
    if current_employee <= 0:
        employees.pop(-1)
        continue
    if current_order > 10:
        pizza_orders.popleft()
        continue

    if current_order <= current_employee:
        employees.pop()
        total_pizza += pizza_orders.popleft()
    elif current_order > current_employee:
        pizza_orders[0] -= current_employee
        total_pizza += current_employee
        employees.pop()
        if pizza_orders[0] <= 0:
            total_pizza += pizza_orders.popleft()


if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    employees = [str(el) for el in employees]
    print(f"Employees: {', '.join(employees)}")
else:
    print("Not all orders are completed.")
    orders = [str(el) for el in pizza_orders]
    print(f"Orders left: {', '.join(orders)}")


