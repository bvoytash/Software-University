data = input().split(", ")

for words in data:
    Flag = False
    if not 3 <= len(words) <= 16:
        continue
    for el in words:
        if not el.isdigit() and not el.isalpha() and el != "-" and el != "_":
            Flag = True
            break
    if Flag:
        continue
    print(words)



