events = input().split("|")

energy = 100
coins = 100
is_valid = True

for i in events:
    event = i.split("-")
    event_name = event[0]
    number = int(event[1])

    if event_name == "rest":
        if energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
        elif energy + number > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
            print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if number <= coins:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            is_valid = False
            break

if is_valid:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
