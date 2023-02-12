def sum_numbers(first, second):
    return first + second


def subtract():
    return sum_numbers(num1, num2) - num3


def add_and_subtract():
    sum_numbers(num1, num2)
    subtract()


num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_nums = 0
print(subtract())
