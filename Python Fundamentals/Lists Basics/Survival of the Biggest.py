
n = input()
amount = int(input())

list_nums = n.split()
new_list = []

for el in list_nums:
    current_num = int(el)
    new_list.append(current_num)

for i in range(0, amount):
    b = min(new_list)
    new_list.remove(b)

print(new_list)

# line = [int(el) for el in input().split()]
# to_remove = int(input())
#
# sorted_line = sorted(line)
# sorted_line = sorted_line[:to_remove]
#
# for el in sorted_line:
#     if el in line:
#         line.remove(el)
#
#
# print(line)