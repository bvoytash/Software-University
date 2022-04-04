import re

data = input().lower()
word = input().lower()

pattern = fr"\b{word}\b"
result = re.findall(pattern, data)
print(len(result))