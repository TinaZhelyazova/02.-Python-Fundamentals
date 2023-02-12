def smallest_number(numbers):
    min_number = float('inf')
    for num in numbers:
        if min_number > num:
            min_number = num
    return min_number


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_number([num1, num2, num3]))
