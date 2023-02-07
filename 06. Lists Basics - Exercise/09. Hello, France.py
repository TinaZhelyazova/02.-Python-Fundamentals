items = input().split("|")
budget = float(input())
starting_budget = budget

train_ticket = 150

clothes_price = 50.00
shoes_price = 35.00
accessories_price = 20.50

new_price = 0
profit = 0
sum_of_new_prices = 0
new_prices_lst = []
sell_products = 0

for item in items:
    commands = item.split("->")
    type_of_item = commands[0]
    price_of_item = float(commands[1])

    if price_of_item <= budget:
        if type_of_item == "Clothes":
            if price_of_item <= clothes_price:
                pass
            else:
                continue
        elif type_of_item == "Shoes":
            if price_of_item <= shoes_price:
                pass
            else:
                continue
        elif type_of_item == "Accessories":
            if price_of_item <= accessories_price:
                pass
            else:
                continue
        budget -= price_of_item
        increased_price = float(price_of_item + price_of_item * 0.40)
        sell_products += increased_price
        new_prices_lst.append(increased_price)

budget += float(sell_products)
profit = budget - starting_budget

print(' '.join('{:0.2f}'.format(i) for i in new_prices_lst))
print(f"Profit: {profit:.2f}")
if budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
