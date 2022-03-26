line = input()

elements = {}
for el in line:
    if el not in elements:
        elements[el] = 1
    else:
        elements[el] += 1
elements = sorted(elements.items(), key=lambda x: x[0])

for el, count in elements:
    print(f"{el}: {count} time/s")