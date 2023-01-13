n = int(input())
sum_of_digits = 0
is_true = ""

for n in range(1, n+1):
    second_digit = n % 10
    first_digit = (n - second_digit) / 10
    sum_of_digits = first_digit + second_digit
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_true = True
        print(f"{n} -> {is_true}")
        sum_of_digits = 0
    else:
        is_true = False
        print(f"{n} -> {is_true}")
        sum_of_digits = 0
