def odd_and_even_sum(numbers):
    odd_sum = 0
    even_sum = 0
    for i in numbers:
        curr_ch = int(i)
        if curr_ch % 2 == 0:
            even_sum += curr_ch
        else:
            odd_sum += curr_ch
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


number = input()
print(odd_and_even_sum(number))
