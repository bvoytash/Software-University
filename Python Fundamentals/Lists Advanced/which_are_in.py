string_1 = input().split(", ")
string_2 = input().split(", ")


substring_list = []

for el in string_1:
    substring = [substring_list.append(el) for string in string_2 if el in string]

print(list(set(substring_list)))