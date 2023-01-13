budget = int(input())
price = input()
bill = 0

while price != "End":
    bill += int(price)
    if bill>budget:
        print(f"You went in overdraft!")
        break
    price = input()

if bill<=budget:
    print(f"You bought everything needed.")