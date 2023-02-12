def order_price(curr_product, number):
    if curr_product == "coffee":
        return number * 1.50
    elif curr_product == "coke":
        return number * 1.40
    elif curr_product == "water":
        return number * 1
    elif curr_product == "snacks":
        return number * 2


products = input()
quantity = int(input())
all_price = order_price(products, quantity)
print(f"{all_price:.2f}")
