tourists = int(input())
wagon_list = [int(el) for el in input().split()]
all_tourists = tourists

for wagon in range(0, len(wagon_list)):
    if tourists >= 4:
        added_tourist = 4 - wagon_list[wagon]
        wagon_list[wagon] = 4
        tourists -= added_tourist
    elif tourists > 0:
        wagon_list[wagon] += tourists
        tourists = 0


max_seats = len(wagon_list) * 4
if sum(wagon_list) == max_seats and tourists == 0:
    wagon_list = [str(el) for el in wagon_list]
    print(" ".join(wagon_list))

elif sum(wagon_list) < max_seats:
    wagon_list = [str(el) for el in wagon_list]
    print(f"The lift has empty spots!")
    print(" ".join(wagon_list))

elif all_tourists > max_seats:
    wagon_list = [str(el) for el in wagon_list]
    print(f"There isn't enough space! {tourists} people in a queue!")
    print(" ".join(wagon_list))




