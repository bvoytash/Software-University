def calculate(command, numbers):
    sum_list = 0
    if command == "Even":
        sum_list = sum([el for el in numbers if el % 2 == 0])
    else:
        sum_list = sum([el for el in numbers if not el % 2 == 0])
    return sum_list * len(numbers)

command = input()
numbers = [int(el) for el in input().split()]

print(calculate(command, numbers))