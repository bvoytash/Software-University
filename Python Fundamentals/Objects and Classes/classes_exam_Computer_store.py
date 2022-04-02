

command = input()

total_price_without = 0
taxes = 0

while not command == "special" and command != "regular":
    price = float(command)

    if price <= 0:
        print("Invalid price!" )
    else:
        total_price_without += price
        taxes += 0.2 * price

    command = input()

final_price = total_price_without + taxes
if command == "special":
    final_price -= (final_price * 0.1)
    if final_price == 0:
        print("Invalid order!" )
    else:
        print ("Congratulations you've just bought a new computer!\n"
                f"Price without taxes: {total_price_without:.2f}$\n"
                f"Taxes: {taxes:.2f}$ \n"
                "-----------\n"
                f"Total price: {final_price:.2f}$")


else:
    if final_price == 0:
        print("Invalid order!" )
    else:
        print(("Congratulations you've just bought a new computer!\n"
                f"Price without taxes: {total_price_without:.2f}$\n"
                f"Taxes: {taxes:.2f}$ \n"
                "-----------\n"
                f"Total price: {final_price:.2f}$"))



