

command = input()
final_list = [0 for _ in range(10)]

while not command == "End":
    todo_list = command.split("-")
    priority = int(todo_list[0])
    todo = todo_list[1]
    final_list.insert(priority, todo)

    command = input()

result = [el for el in final_list if not el == 0]
print(result)

