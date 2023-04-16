command = input()
bakery = {}

while True:
    if command == "statistics":
        break

    lines = command.split(": ")
    product = lines[0]
    quantity = int(lines[1])

    if product not in bakery:
        bakery[product] = quantity
    else:
        bakery[product] += quantity
    command = input()

print(f"Products in stock:")
for items in bakery:
    print(f"- {items}: {bakery[items]}")
print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")



