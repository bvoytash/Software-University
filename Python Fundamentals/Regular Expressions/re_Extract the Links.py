import re

data = input()
pattern = r"www\.(?P<domain>[a-zA-Z0-9-]+)\.(?P<domain_block>\.?[a-z]+)+\b"
while not data == "":
    link_site = re.finditer(pattern, data)
    result = [obj.group() for obj in link_site]
    if result:
        print(*result)
    data = input()