def first(n_1):
    line_1 = set()
    for i in range(n_1):
        number = int(input())
        line_1.add(number)
    return line_1

def second(n_2):
    line_2 = set()
    for i in range(n_2):
        number = int(input())
        line_2.add(number)
    return line_2
data = input().split()
n_1 = int(data[0])
n_2 =int(data[1])

first_line = first(n_1)
second_line = second(n_2)
common = first_line.intersection(second_line)
for i in common:
    print(i)