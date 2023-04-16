prices = {}
quantities = {}
while True:
    command = input()

    if command == "buy":

        break
    args = command.split()
    name = args[0]
    price = float(args[1])
    quantity = int(args[2])

    if name not in prices:
        prices[name] = price
        quantities[name] = quantity
    else:
        prices[name] = price
        quantities[name] += quantity

for i in prices:
    final_price = prices[i]*quantities[i]
    print(f"{i} -> {final_price:.2f}")
