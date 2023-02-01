factor = int(input())
count = int(input())
list_of_numbers = []

for i in range(1, count+1):
    list_of_numbers.append(factor*i)

print(list_of_numbers)