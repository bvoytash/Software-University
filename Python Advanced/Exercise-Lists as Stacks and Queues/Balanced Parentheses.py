line = input()

#{[()]}
my_dict = {"(": ")", "[": "]", "{": "}"}

open_stack = []

Flag = True
for el in line:
    if el in "([{":
        open_stack.append(el)
    else:
        if len(open_stack) > 0:
            if el == my_dict[open_stack[-1]]:
                open_stack.pop()
            else:
                Flag = False
                break
        else:
            Flag = False
            break

if Flag:
    print("YES")
else:
    print("NO")

