n = int(input())
the_length = {}
for i in range(n):
    data = input().split("-")
    first_start = int(data[0].split(",")[0])
    first_end = int(data[0].split(",")[1])
    first_list = []
    second_start = int(data[1].split(",")[0])
    second_end = int(data[1].split(",")[1])
    second_list = []
    for number in range(first_start, first_end + 1):
        first_list.append(number)
    for number in range(second_start, second_end + 1):
        second_list.append(number)
    first_set = set(first_list)
    second_set = set(second_list)
    a = list(first_set.intersection(second_set))
    the_length[len(a)] = a

sorted_dict = sorted(the_length.items(), key=lambda x: x[0], reverse=True)
max_length = []
for el in sorted_dict[0][1]:
    max_length.append(el)

print(f"Longest intersection is {max_length} with length {len(max_length)}")



