import re

data = input()
result = []
while data:
    pattern = r"\d+"
    numbers = re.findall(pattern, data)
    # numbers = [num.group() for num in numbers]
    if numbers:
        print(*numbers, end=" ")
    data = input()
