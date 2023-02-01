numbers = input().split(" ")
int_nums = []
for i in range(len(numbers)):
    current_number = int(numbers[i])
    int_nums.append(current_number * -1)

print(int_nums)
