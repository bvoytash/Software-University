dict_products = {}

data = input()
while not data == "buy":
    product = data.split()[0]
    price = float(data.split()[1])
    quantity = float(data.split()[2])
    if not product in dict_products:
        dict_products[product] = [price, quantity]
    else:
        dict_products[product][1] += quantity
        if dict_products[product][0] != price:
            dict_products[product][0] = price

    data = input()

for key, value in dict_products.items():
    total_price = dict_products[key][0] * dict_products[key][1]
    print(f"{key} -> {total_price:.2f}")

