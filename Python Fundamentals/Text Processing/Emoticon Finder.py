data = input()

for index, el in enumerate(data):
    if el == ":":
        print(el + data[index + 1])