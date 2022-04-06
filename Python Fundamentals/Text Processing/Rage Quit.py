data = input()

current_string = ""
final_string = ""
index = 0

while index < len(data):
    if not data[index].isdigit():
        current_string += data[index]
        index += 1
    else:
        number = ""
        while index < len(data) and data[index].isdigit():
            number += data[index]
            index += 1
            if index == len(data):
                break

        number = int(number)
        current_string = current_string.upper() * number
        final_string += current_string
        current_string = ""


print(f"Unique symbols used: {len(set(final_string))}")
print(f"{final_string}")






