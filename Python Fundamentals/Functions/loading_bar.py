

def loading_bar(number):
    symbols = number // 10
    points = 10 - symbols
    if number < 100:
        loading = f"{number}% [" + ("%" * symbols + "." * points) + "]"
        print(loading)
        print("Still loading...")
    elif number == 100:
        print("100% Complete!")
        print("[" + ("%" * symbols + "." * points) + "]")



num = int(input())
loading_bar(num)
