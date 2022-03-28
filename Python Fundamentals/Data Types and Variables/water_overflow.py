n = int(input())
total = 0
final_pour = 0
counter = 0
for tank in range(0, n):
    current_pour = int(input())
    total += current_pour
    if counter > 0:
        if total > 255:
            total -= current_pour
            print("Insufficient capacity!")
            continue

    if total > 255:
        print("Insufficient capacity!")
        total -= current_pour
        counter = 1
print(total)