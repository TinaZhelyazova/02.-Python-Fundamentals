time = [int(x) for x in input().split()]
left_side = time[0: len(time)//2]
right_side = time[len(time)//2+1:]
right_sum = 0
left_sum = 0
for i in left_side:
    left_sum += i
    if i == 0:
        left_sum *= 0.8
for j in reversed(right_side):
    right_sum += j
    if j == 0:
        right_sum *= 0.8

if right_sum < left_sum:
    print(f"The winner is right with total time: {right_sum:.1f}")
else:
    print(f"The winner is left with total time: {left_sum:.1f}")

