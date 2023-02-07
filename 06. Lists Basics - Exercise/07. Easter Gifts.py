gifts = input().split(" ")
commands = input().split(" ")

while commands[0] != "No" and commands[1] != "Money":
    command = commands[0]
    gift = commands[1]

    for i in gifts:
        if command == "OutOfStock":
            while gift in gifts:
                gift_index = gifts.index(gift)
                word = "None"
                gifts.insert(gift_index, word)
                gifts.remove(gift)
            break
        elif command == "JustInCase":
            gifts[-1] = gift
            break
        elif command == "Required":
            idx = int(commands[2])
            if idx in range(len(gifts)):
                gifts[idx] = gift
                break
    commands = input().split(" ")

while "None" in gifts:
    gifts.remove("None")
print(" ".join(gifts))
