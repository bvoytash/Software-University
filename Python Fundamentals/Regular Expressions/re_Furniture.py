import re

command = input()
furniture = []
total_price = 0
pattern = r"((^>{2})|(?<=\s>{2}))(?P<item>[a-zA-Z]+)<<(?P<price>\d+\.?\d*)\!(?P<quantity>\d+)\b"
while not command == "Purchase":
    match_obj = re.match(pattern, command)
    if match_obj:
        data = match_obj.groupdict()
        furniture.append(data["item"])
        total_price += float(data["price"]) * int((data["quantity"]))
    command = input()

print("Bought furniture:")
for el in furniture:
    print(el)
print(f"Total money spend: {total_price:.2f}")

# import re
# command = input()
# furniture = []
# total_price = 0
# while not command == "Purchase":
#     price_int = 0
#     quantity_int = 0
#     item_pattern = r"\b[A-Z]+[a-z]*\b"
#     item = re.findall(item_pattern, command)
#
#     price_pattern = r"\b\d+\.?\d+\b"
#     price = re.findall(price_pattern, command)
#     if price:
#         price_int = float(price[0])
#
#     quantity_pattern = r"(?<=!)\d+\b"
#     quantity = re.findall(quantity_pattern, command)
#     if quantity:
#         quantity_int = int(quantity[0])
#         total_price += (price_int * quantity_int)
#
#     if price_int !=0 and quantity_int != 0:
#         item_string = item[0]
#         furniture.append(item_string)
#
#     command = input()
#
# print("Bought furniture:")
# for el in furniture:
#     print(el)
# print(f"Total money spend: {total_price:.2f}")
