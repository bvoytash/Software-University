resource = input()
my_dict = {}
while not resource == "stop":
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity
    resource = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")