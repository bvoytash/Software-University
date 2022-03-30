numbers_string = input().split(", ")
int_list = [int(el) for el in numbers_string]

# even_list_index = [index for index, nums in enumerate(int_list) if nums % 2 == 0]
# print(even_list_index)


even_list = list(filter(lambda index: int_list[index] % 2 == 0, range(len(int_list))))
print(even_list)