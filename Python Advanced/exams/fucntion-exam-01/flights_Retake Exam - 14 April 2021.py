def flights(*args):
    my_dict = {}
    for index, el in enumerate(args):
        if not el == "Finish":
            if isinstance(el, str):
                if not el in my_dict:
                    my_dict[el] = args[index + 1]
                else:
                    my_dict[el] += args[index + 1]
        else:
            return my_dict
    return my_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))