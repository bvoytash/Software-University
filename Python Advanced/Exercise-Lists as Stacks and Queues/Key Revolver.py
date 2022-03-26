from collections import deque

bullet_price = int(input())
gun_barrel = int(input())

bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
intelligence = int(input())

locks = deque(locks)
shoot_bullets = 0
for shots in range(1, len(bullets) + 1):

    concurrent_bullet = bullets.pop()
    shoot_bullets += 1
    if concurrent_bullet > locks[0]:
        print("Ping!")
    else:
        locks.popleft()
        print("Bang!")

    if bullets and shots % gun_barrel == 0:
        print("Reloading!")

    if not locks:
        money_earned = intelligence - ( shoot_bullets * bullet_price)
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")