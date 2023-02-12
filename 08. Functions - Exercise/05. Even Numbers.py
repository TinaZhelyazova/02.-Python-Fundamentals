def even_numbers_filter(num):
    result = num % 2 == 0
    return result


numbers_as_strings = input().split(" ")
numbers_as_integers = list(map(int, numbers_as_strings))
print(list(filter(even_numbers_filter, numbers_as_integers)))
