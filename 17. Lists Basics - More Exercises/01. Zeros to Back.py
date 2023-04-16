numbers_as_numbers = [int(x) for x in input().split(", ")]
zeros = []
non_zeros = []
for number in numbers_as_numbers:
    if number == 0:
        zeros.append(number)
    else:
        non_zeros.append(number)

non_zeros += zeros

print(non_zeros)
