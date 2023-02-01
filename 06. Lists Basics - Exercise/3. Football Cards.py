team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
red_cards = input().split(" ")
terminated_game = False

for red_card in red_cards:
    if red_card in team_a:
        team_a.remove(red_card)
        if len(team_a) < 7:
            terminated_game = True
            break
    elif red_card in team_b:
        team_b.remove(red_card)
        if len(team_b) < 7:
            terminated_game = True
            break
if terminated_game == True:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
