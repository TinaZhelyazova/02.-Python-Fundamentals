cards = input().split(" ")
shuffles = int(input())
#final_deck = []

for shuffle in range(shuffles):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    left_part = cards[0: middle_of_the_deck]
    right_part = cards[middle_of_the_deck::]
    for card in range(len(right_part)):
        final_deck.append(left_part[card])
        final_deck.append(right_part[card])

    cards = final_deck

print(cards)

