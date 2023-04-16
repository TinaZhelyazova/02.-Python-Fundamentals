text = input().split()
numbers = []
sum_numbers = []
for i in range(len(text)):
    first_letter = text[i][0]
    second_letter = text[i][-1]
    number1 = text[i].replace(first_letter, "")
    number = int(number1.replace(second_letter, ""))
    if first_letter.isupper():
        first_sum_upper = number / (ord(first_letter) & 31)
        numbers.append(first_sum_upper)
    else:
        first_sum_lower = number * (ord(first_letter) & 31)
        numbers.append(first_sum_lower)

    if second_letter.isupper():
        second_sum_upper = numbers[0] - (ord(second_letter) & 31)
        sum_numbers.append(second_sum_upper)
        numbers.pop()
    else:
        second_sum_lower = numbers[0] + (ord(second_letter) & 31)
        sum_numbers.append(second_sum_lower)
        numbers.pop()

print(f"{sum(sum_numbers):.2f}")

# for i in text:
#    print((ord(i) & 31), end="")
