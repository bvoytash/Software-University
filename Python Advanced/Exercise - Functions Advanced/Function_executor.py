def func_executor(*args):
    the_list = []
    for tt in args:
        func = tt[0]
        the_list.append(func(int(tt[1][0]), int(tt[1][1])))
    return the_list


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2))))
print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
print(func_executor((multiply_numbers, (2, 4))))
