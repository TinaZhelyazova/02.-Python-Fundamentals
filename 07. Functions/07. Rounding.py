#result = list(map(lambda x: round(float(x)), input().split(" ")))
#print(result)

numbers_as_strings = input().split(" ")
numbers_as_nums = list(map(float, numbers_as_strings))
rounded_nums = []

for num in numbers_as_nums:
    rounded_nums.append(round(num))

print(rounded_nums)
