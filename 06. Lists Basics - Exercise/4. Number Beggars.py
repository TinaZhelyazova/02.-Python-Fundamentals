money_for_beggar = input().split(", ")
beggar = int(input())
constbeggar = beggar
beggar_count = beggar
money_taken = []
sum_of_money = 0
money_each_beggar = []
starting_index = 0

for money_index in range(len(money_for_beggar)):
    cuurrent_money = int(money_for_beggar[money_index])
    money_taken.append(cuurrent_money)

while beggar != 0:
    for i in range(starting_index, len(money_for_beggar), constbeggar):
        sum_of_money += money_taken[i]
    money_each_beggar.append(sum_of_money)
    beggar -= 1
    sum_of_money = 0
    starting_index += 1
print(f"{money_each_beggar}")
