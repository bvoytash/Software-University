import re

data = input()
pattern = r"(?<=\s)\b([a-z]|[\d])+([\.|_|-])?([a-z]|[\d])+@(?P<first_word>[a-z]+[-|]?[a-z]*)\.(?P<second_word>[a-z]+[-|]?[a-z]*)\.?(?P<host>[a-z]+)\b"
email = re.finditer(pattern, data)
list_emails = [el.group() for el in email]
for el in list_emails:
    print(el)