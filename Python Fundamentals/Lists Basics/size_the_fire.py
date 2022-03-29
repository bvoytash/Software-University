fire_cells = input().split("#")
water = int(input())

total_fire = 0
print("Cells:")

for fire in fire_cells:
    type_of_fire, value = fire.split(" = ")
    current_fire = int(value)

    if type_of_fire == "High":
        if 80 < current_fire <= 125 and water >= current_fire:
            total_fire += current_fire
            water -= current_fire
            print(f" - {value}")
    elif type_of_fire == "Medium" and water >= current_fire:
        if 50 < current_fire <= 80:
            total_fire += current_fire
            water -= current_fire
            print(f" - {value}")
    elif type_of_fire == "Low" and water >= current_fire:
        if 0 < current_fire <= 50:
            total_fire += current_fire
            water -= current_fire
            print(f" - {value}")
    else:
        continue

effort = 0.25 * total_fire
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


# fire_cell = input().split("#")
# water = int(input())
# total_fire = 0
# effort = 0
# print("Cells:")
# for fire in fire_cell:
#     type = fire.split()[0]
#     cell = int(fire.split()[-1])
#     if not water >= cell:
#         continue
#
#     if type == "High":
#         if 80 < cell < 126:
#             water -= cell
#             total_fire += cell
#             effort += 0.25 * cell
#             print(f"- {cell}")
#     if type == "Medium":
#         if 50 < cell < 81:
#             water -= cell
#             total_fire += cell
#             effort += 0.25 * cell
#             print(f"- {cell}")
#     if type == "Low":
#         if 0 < cell < 51:
#             water -= cell
#             total_fire += cell
#             effort += 0.25 * cell
#             print(f"- {cell}")
#
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")