word_str = input()

my_list = word_str.split()
new_list = []
for el in my_list:
    num = int(el)
    if num > 0:
        result = num - (2 * num)
        new_list.append(result)
    if num < 0:
        result = num + abs(2 * num)
        new_list.append(result)
    if num == 0:
        result = 0
        new_list.append(result)
print(new_list)
