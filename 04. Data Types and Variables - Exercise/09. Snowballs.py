number_of_snowballs = int(input())

curr_value = 0
prev_value = 0
value = 0
highest_weight = 0
highest_time = 0
snowball_quality = 0

for i in range(0, number_of_snowballs):
    weight_of_ball = int(input())
    time_needed_to_target = int(input())
    quality = int(input())

    curr_value = (weight_of_ball / time_needed_to_target) ** quality
    if curr_value >= prev_value:
        snowball_quality = quality
        highest_time = time_needed_to_target
        highest_weight = weight_of_ball
        value = curr_value
        prev_value = curr_value
        curr_value = 0

print(f"{highest_weight} : {highest_time} = {int(value)} ({snowball_quality})")

