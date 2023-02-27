numbers = [int(num) for num in input().split(", ")]
positive_numbers = list(filter(lambda x: x >= 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Positive: {', '.join(str(num) for num in positive_numbers)}")
print(f"Negative: {', '.join(str(num) for num in negative_numbers)}")
print(f"Even: {', '.join(str(num) for num in even_numbers)}")
print(f"Odd: {', '.join(str(num) for num in odd_numbers)}")
