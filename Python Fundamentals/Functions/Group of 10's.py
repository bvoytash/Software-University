numbers = [int(el) for el in input().split(", ")]

group = 10
max_number = max(numbers)

while numbers:
    current_group = []
    for el in numbers:
        if group - 10 < el <= group:
            current_group.append(el)

    for el in current_group:
        numbers.remove(el)

    print(f"Group of {group}'s: {current_group}")
    group += 10
