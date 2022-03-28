fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_counter = 0
expenses = 0

for fight in range(1, fights + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 3 == 0 and fight % 2 == 0:
        expenses += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

# lose_battle = int(input())
#
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# brakes = {"helmet": 0, "sword": 0, "shield": 0, "armor": 0}
# counter = 0
# for battle in range(1, lose_battle + 1):
#     if battle % 2 == 0:
#         brakes["helmet"] += 1
#     if battle % 3 == 0:
#         brakes["sword"] += 1
#         if battle % 2 == 0:
#             brakes["shield"] += 1
#             counter += 1
#             if counter % 2 == 0:
#                 brakes["armor"] += 1
#                 counter = 0
#
# total_price = brakes["helmet"] * helmet_price + brakes["shield"] * shield_price + brakes["sword"] * sword_price + brakes["armor"] * armor_price
#
# print(f"Gladiator expenses: {total_price:.2f} aureus")