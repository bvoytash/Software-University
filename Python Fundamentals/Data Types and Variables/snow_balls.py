num_snowballs = int(input())

max_value = 0
a = 0
b = 0
c = 0

for ball in range(1, num_snowballs + 1 ):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > max_value:
        max_value = snowball_value
        a = snowball_snow
        b = snowball_time
        c = snowball_quality

print(f"{a} : {b} = {int(max_value)} ({c})")