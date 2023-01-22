n = int(input())
command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'

list_of_numbers = []

for i in range(n):
    curr_number = int(input())
    list_of_numbers.append(curr_number)

command = input()
filtered_numbers = []

for number in list_of_numbers:
    filtered_passes = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_positive and number >= 0) or
        (command == command_negative and number < 0)
    )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)
