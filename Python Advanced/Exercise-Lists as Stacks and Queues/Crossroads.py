from collections import deque
green_light = int(input())
free_window = int(input())

my_cars = deque([])
Flag = True
command = input()
car_passed = []
while not command == "END":
    time = 0
    if command == "green":
        time = green_light
        while time and my_cars:
            current_car = my_cars[0]

            if len(current_car) <= time:
                passed = my_cars.popleft()
                car_passed.append(passed)
                time -= len(current_car)

            elif len(current_car) > time:
                if len(current_car) - time <= free_window:
                    passed = my_cars.popleft()
                    car_passed.append(passed)
                    time = 0
                else:
                    hit = (time + free_window)
                    hit_letter = current_car[hit]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {hit_letter}.")
                    Flag = False
                    break
        if not Flag:
            break
    else:
        my_cars.append(command)
    command = input()

if Flag:
    print("Everyone is safe.")
    total_cars = len(car_passed)
    print(f"{total_cars} total cars passed the crossroads.")