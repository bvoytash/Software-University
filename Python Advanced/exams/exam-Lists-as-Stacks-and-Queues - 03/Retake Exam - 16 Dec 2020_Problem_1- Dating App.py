from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])


matches = 0
while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop(-1)
        continue

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop(-1)
        males.pop(-1)
        continue

    if males and females:
        if females[0] == males[-1]:
            females.popleft()
            males.pop(-1)
            matches += 1
        else:
            females.popleft()
            males[-1] -= 2
            if males[-1] <= 0:
                males.pop(-1)


print(f"Matches: {matches}")
if males:
    males = reversed([str(el) for el in males])
    print(f"Males left: {', '.join(males)}")
else:
    print("Males left: none")

if females:
    females = [str(el) for el in females]
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")
