data = input().split()
dict_data = {}

for el in data:
    for letter in el:
        if not letter in dict_data:
            dict_data[letter] = 1
        else:
            dict_data[letter] += 1

for key, value in dict_data.items():
    print(f"{key} -> {value}")