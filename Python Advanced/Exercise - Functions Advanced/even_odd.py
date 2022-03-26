def even_odd(*args):
    my_list = []
    if args[-1] == "even":
        my_list = [el for el in args[:-1] if el % 2 == 0]
    else:
        my_list = [el for el in args[:-1] if not el % 2 == 0]
    return my_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))