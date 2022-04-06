data = list(input())
explode = 0
data_copy = data.copy()
for index in range(0, len(data)):
    if index < len(data):
        if data[index] == ">":
            explode += int(data[index + 1])

        if data[index] != ">" and explode > 0:
            data.pop(index)
            explode -= 1
            continue
    else:
        break

    if index + 1 < len(data):
        if data[index + 1] != ">":
            if explode:
                data.pop(index + 1)
                explode -= 1
    else:
        break

print("".join(data))