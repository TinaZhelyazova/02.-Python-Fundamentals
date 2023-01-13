budget = float(input())
price_for_flour = float(input())
price_of_eggs = price_for_flour*0.75
price_of_milk = price_for_flour+(price_for_flour*0.25)
money_for_loaf = price_for_flour+price_of_eggs+(price_of_milk/4)
loaves = 0
colored_eggs = 0

while budget > money_for_loaf:
    if budget > money_for_loaf:
        budget -= money_for_loaf
        loaves += 1
        colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves-2



print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
