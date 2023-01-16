number_of_lines = int(input())
capacity = 255
all_water = 0

for i in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water > capacity:
        print("Insufficient capacity!")
    elif liters_of_water <= capacity:
        capacity -= liters_of_water
        all_water += liters_of_water
print(all_water)

