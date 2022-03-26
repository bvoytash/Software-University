n = int(input())
my_stack = []
for i in range(0, n):
    command = input().split()
    action = int(command[0])

    if action == 1:
        number = int(command[1])
        my_stack.append(number)
    elif action == 2:
        if my_stack:
            my_stack.pop()
    elif action == 3:
        if my_stack:
            print(max(my_stack))
    elif action == 4:
        if my_stack:
            print(min(my_stack))

my_stack = reversed([str(el) for el in my_stack])
print(", ".join(my_stack))
