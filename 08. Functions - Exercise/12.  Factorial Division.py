def factorial_numbers(number_one,number_two):
    sum_of_first_factorial = 1
    sum_of_second_factorial = 1

    for i in range(number_one, 1, -1):
        sum_of_first_factorial *= i

    for j in range(number_two, 1, -1):
        sum_of_second_factorial *= j

    divided_sum = abs(sum_of_first_factorial // sum_of_second_factorial)
    return f'{divided_sum:.2f}'


num1 = int(input())
num2 = int(input())
print(factorial_numbers(num1, num2))

