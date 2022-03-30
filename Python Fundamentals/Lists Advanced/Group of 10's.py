a = int(input())

if a % 10 > 0:
    max_num = ((a // 10) + 1) * 10
elif a % 10 == 0:
    max_num = a


print(max_num)

if (max_num - 10) < current_num < max_num:
    pass