data = input().split()
my_list = []
for string in data:
    left_side = 0
    right_side = 0
    string = string.strip()
    the_number = int(string[1:-1])

    if string[0].isupper():
        letter = string[0].lower()
        position = (ord(letter) - 97) + 1
        left_side = the_number / position

    elif string[0].islower():
        letter = string[0]
        position = (ord(letter) - 97) + 1
        left_side = the_number * position

    if string[-1].isupper():
        letter = string[-1].lower()
        position = (ord(letter) - 97) + 1
        right_side = left_side - position

    elif string[-1].islower():
        letter = string[-1]
        position = (ord(letter) - 97) + 1
        right_side = left_side + position

    my_list.append(right_side)

the_result = sum(my_list)
print(f"{the_result:.2f}")




