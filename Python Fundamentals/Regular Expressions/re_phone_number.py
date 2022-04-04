import re

data = input()
pattern = r"\+359(\s|-)2\1[0-9]{3}\1[0-9]{4}\b"
number = re.finditer(pattern, data)
numbers = [n.group() for n in number]
print(", ".join(numbers))