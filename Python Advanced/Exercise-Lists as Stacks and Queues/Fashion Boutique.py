line = input().split()
items_in_box = [int(el) for el in line]
rack_capacity = int(input())
needed_racks = 1

current_rack = rack_capacity
while items_in_box:
    current = items_in_box.pop()
    if current_rack >= current:
        current_rack -= current
    else:
        needed_racks += 1
        current_rack = rack_capacity
        current_rack -= current

print(needed_racks)

