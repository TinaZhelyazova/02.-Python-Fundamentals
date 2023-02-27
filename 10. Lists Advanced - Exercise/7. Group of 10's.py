import math

number_sequence = list(map(int, input().split(", ")))
max_num = max(number_sequence)
number_of_groups = math.ceil(max_num/10)
group_num = 1
next_num = 10

for i in range(number_of_groups):
    filtered_numbers = list(filter(lambda x: group_num <= x <= next_num, number_sequence))

    print(f"Group of {i+1}0's: {filtered_numbers}")
    group_num += 10
    next_num += 10

