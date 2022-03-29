numbers = input()
beggars = int(input())

number_list = []
elements = 0
nums = numbers.split(", ")
for el in nums:
    elements += 1
    num = int(el)
    number_list.append(num)

if beggars == len(number_list):
    print(number_list)

if beggars > len(number_list):
    diff = beggars - elements
    for i in range(0, diff):
        number_list.append(0)
    print(number_list)

beggars_list = []
index = 0
if beggars < len(number_list):

    for i in range(beggars):
        beggars_list.append(0)

    for nums in number_list:
        beggars_list[index] += nums
        index += 1
        if index == beggars:
            index = 0
    print(beggars_list)





