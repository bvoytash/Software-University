data = input()
unique_el = []
for index in range(len(data)):
    if index + 1 < len(data):
        if data[index] == data[index + 1]:
            continue
        else:
            unique_el.append(data[index])
    else:
        unique_el.append(data[index])

print("".join(unique_el))