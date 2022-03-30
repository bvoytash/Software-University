version = [int(el) for el in input().split(".")]

if version[-1] < 9:
    version[-1] += 1
else:
    version[-1] = 0
    if version[1] < 9:
        version[1] += 1
    else:
        version[1] = 0
        version[0] += 1

version = [str(el) for el in version]
print(".".join(version))