def operations(num):
    min_number = min(num)
    max_number = max(num)
    sum_of_numbers = sum(num)
    return f'The minimum number is {min_number} \n' \
           f"The maximum number is {max_number} \n" \
           f"The sum number is: {sum_of_numbers}"


numbers = [int(x) for x in input().split(" ")]
print(operations(numbers))
