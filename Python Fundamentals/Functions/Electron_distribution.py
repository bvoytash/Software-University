shell = int(input())

list_shell = []
index = 1
while shell > 0:
    number = 2*index**2
    index += 1
    if shell >= number:
        list_shell.append(number)
        shell -= number
    else:
        list_shell.append(shell)
        shell = 0

print(list_shell)


