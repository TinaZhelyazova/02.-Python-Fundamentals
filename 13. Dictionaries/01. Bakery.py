input_food = input().split()

dict_food = {input_food[i]: int(input_food[i+1]) for i in range(0, len(input_food), 2)}
print(dict_food)
