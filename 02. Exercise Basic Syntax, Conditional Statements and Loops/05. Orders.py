number_of_orders = int(input())
price = 0
final_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    price = price_per_capsule*days*capsules_needed_per_day

    if price_per_capsule < 0.01  or price_per_capsule>100:
        continue
    elif days <1 or days >31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day >2000:
        continue
    elif price == 0:
        continue
    print(f"The price for the coffee is: ${price:.2f}")
    final_price += price

print(f"Total: ${final_price:.2f}")

