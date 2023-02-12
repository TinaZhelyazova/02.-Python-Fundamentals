numbers = input().split(" ")
lst_nums = []

for num in numbers:
    lst_nums.append(abs(float(num)))

print(lst_nums)
