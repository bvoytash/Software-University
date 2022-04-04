import re

data = input()
pattern = r"\b_([A-Z]|[a-z]|\d)+\b"

result = re.finditer(pattern, data)
result = [el.group() for el in result]

final_result = []
for el in result:
   el = el.replace("_", "")
   final_result.append(el)
print(",".join(final_result))
