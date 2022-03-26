def concatenate(*args):
    my_list = []
    for el in args:
        my_list.append(el)
    return "".join(my_list)

print(concatenate("Soft", "Uni", "Is", "Great", "!"))