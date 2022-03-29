def last(reversed_array, number, even_odd):
    int_list = [int(el) for el in reversed_array]
    last_even = []
    last_odd = []
    for num in (int_list[::-1]):
        if num % 2 == 0:
            if len(last_even) < number:
                last_even.append(num)
        else:
            if len(last_odd) < number:
                last_odd.append(num)
    if even_odd == "even":
        if len(int_list) < number:
            print("Invalid count")
        elif len(last_even) == 0:
            print("[]")
        else:
            print(last_even)
    if even_odd == "odd":
        if len(int_list) < number:
            print("Invalid count")
        elif len(last_odd) == 0:
            print("[]")
        else:
            print(last_odd)

def first(reversed_array, number, even_odd):
    int_list = [int(el) for el in reversed_array]
    first_even = []
    first_odd = []
    for num in int_list:
        if num % 2 == 0:
            if len(first_even) < number:
                first_even.append(num)
        else:
            if len(first_odd) < number:
                first_odd.append(num)
    if even_odd == "even":
        if len(int_list) < number:
            print("Invalid count")
        elif len(first_even) == 0:
            print("[]")
        else:
            print(first_even)
    if even_odd == "odd":
        if len(int_list) < number:
            print("Invalid count")
        elif len(first_odd) == 0:
            print("[]")
        else:
            print(first_odd)


def min(array_list):
    int_list = [int(el) for el in array_list]
    min_even = 2**31
    min_odd = 2**31
    for num in int_list:
        if num % 2 == 0:
            if num < min_even:
                min_even = num
        else:
            if num < min_odd:
                min_odd = num
    if command.split()[1] == "even":
        if min_even != 2**31:
            result_even = int_list.index(min_even)
            print(result_even)
        else:
            print("No matches")
    elif command.split()[1] == "odd":
        if min_odd != 2**31:
            result_odd = int_list.index(min_odd)
            print(result_odd)
        else:
            print("No matches")

def max(array_list):
    int_list = [int(el) for el in array_list]
    max_even = 0
    max_odd = 0
    for num in int_list:
        if num % 2 == 0:
            if num > max_even:
                max_even = num
        else:
            if num > max_odd:
                max_odd = num
    if command.split()[1] == "even":
        if max_even != 0:
            result_even = int_list.index(max_even)
            print(result_even)
        else:
            print("No matches")
    elif command.split()[1] == "odd":
        if max_odd != 0:
            result_odd = int_list.index(max_odd)
            print(result_odd)
        else:
            print("No matches")

def exchange_list(array_list, exchange_index):
    if len(array_list) < exchange_index:
        result = "Invalid index"
        return result
    else:
        reversed_list = (array_list[:exchange_index:-1])[::-1]
        b = array_list[:exchange_index + 1:]
        reversed_list.extend(b)
        return reversed_list



array_list = input().split()
command = input()
reversed_array = []
counter = 0
while not command == "end":
    if "exchange" in command:
        exchange_index = int(command.split()[1])
        exchange_list(array_list, exchange_index)
        if exchange_list(array_list, exchange_index) == "Invalid index":
            print("Invalid index")
        else:
            array_list = (exchange_list(array_list, exchange_index))
            reversed_array = array_list

    if "max" in command:
        if command.split()[1] == "even":
            max(array_list)
        elif command.split()[1] == "odd":
            max(array_list)

    if "min" in command:
        if command.split()[1] == "even":
            min(array_list)
        elif command.split()[1] == "odd":
            min(array_list)

    if "first" in command:
        number = int(command.split()[1])
        even_odd = command.split()[2]
        first(array_list, number, even_odd)

    if "last" in command:
        number = int(command.split()[1])
        even_odd = command.split()[2]
        last(array_list, number, even_odd)


    command = input()

final_print = [int(el) for el in reversed_array]
print(final_print)