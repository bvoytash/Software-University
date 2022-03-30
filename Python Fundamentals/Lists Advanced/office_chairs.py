rooms = int(input())
free_chairs = 0
need_more_chairs = 0
for room in range(1, rooms + 1):
    data = input()
    chairs = len(data.split()[0])
    people = int(data.split()[1])
    if people > chairs:
        diff = people - chairs
        need_more_chairs += diff
        print(f"{diff} more chairs needed in room {room}")
    else:
        free_chairs += (chairs - people)
if need_more_chairs == 0:
    print(f"Game On, {free_chairs} free chairs left")
