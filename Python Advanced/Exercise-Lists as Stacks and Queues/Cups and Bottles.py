from collections import deque

cups = list(map(int, input().split()))
water = list(map(int, input().split()))
cups = deque(cups)
wasted_water = []

while water and cups:
    if water[-1] > cups[0]:
        water[-1] -= cups[0]
        wasted_water.append(water.pop())
        cups.popleft()

    elif water[-1] == cups[0]:
        water.pop()
        cups.popleft()

    elif water[-1] < cups[0]:

        while cups[0] > 0:
            if water[-1] < cups[0]:
                cups[0] -= water[-1]
                water.pop()
                if not water:
                    break
            else:
                water[-1] -= cups[0]
                wasted_water.append(water.pop())
                cups[0] = 0

                if cups[0] == 0:
                    cups.popleft()
                    break
if water:
    water = list(map(str, water))
    print(f"Bottles: {' '.join(water)}")
if cups:
    cups = list(map(str, cups))
    print(f"Cups: {' '.join(cups)}")
print(f"Wasted litters of water: {sum(wasted_water)}")
