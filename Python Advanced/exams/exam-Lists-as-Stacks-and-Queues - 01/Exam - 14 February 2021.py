from collections import deque
firework = deque([int(el) for el in input().split(", ")])
explosive = [int(el) for el in input().split(", ")]

Palm = 0
Willow = 0
Crossette = 0
Win = False
while firework and explosive:
    if firework[0] <= 0:
        firework.popleft()
        continue
    if explosive[-1] <= 0:
        explosive.pop()
        continue
    current_couple = firework[0] + explosive[-1]

    if current_couple % 3 == 0 and current_couple % 5 != 0:
        Palm += 1
        firework.popleft()
        explosive.pop()
    elif current_couple % 5 == 0 and current_couple % 3 != 0:
        Willow += 1
        firework.popleft()
        explosive.pop()
    elif current_couple % 5 == 0 and current_couple % 3 == 0:
        Crossette += 1
        firework.popleft()
        explosive.pop()
    else:
        firework[0] -= 1
        firework.append(firework[0])
        firework.popleft()

    if Palm >= 3 and Crossette >= 3 and Willow >= 3:
        Win = True
        break

if Win:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework:
    firework = [str(el) for el in firework]
    print(f"Firework Effects left: {', '.join(firework)}")
if explosive:
    explosive = [str(el) for el in explosive]
    print(f"Explosive Power left: {', '.join(explosive)}")

print(f"Palm Fireworks: {Palm}")
print(f"Willow Fireworks: {Willow}")
print(f"Crossette Fireworks: {Crossette}")