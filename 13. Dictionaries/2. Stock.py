pairs = input().split(" ")
search_products = input(). split(" ")

bakery = {pairs[i]: int(pairs[i+1]) for i in range(0, len(pairs), 2)}

for item in search_products:
    if item not in bakery:
        print(f"Sorry, we don't have {item}")
    else:
        print(f"We have {bakery[item]} of {item} left")