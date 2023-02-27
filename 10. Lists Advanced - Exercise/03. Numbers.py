
numbers = [int(x) for x in input().split(" ")]
average_number = (sum(numbers)) / len(numbers)
greater_numbers = []

for i in range(len(numbers)):
    if numbers[i] > average_number:
        greater_numbers.append(numbers[i])  # тук добавяме всвички най-големи числа

if len(greater_numbers) <= 5:  # ако числата са по-малко от 5 трябва да ги принтираме всички
    greater_numbers = sorted(greater_numbers)
elif len(greater_numbers) > 5:
    while len(greater_numbers) != 5:
        greater_numbers = sorted(greater_numbers)
        greater_numbers.pop(0)

# ако има само едно число, ако няма по-голямо число от авереджа
if len(numbers) == 1 or numbers[:-1] == numbers[1:]:
    print("No")
print(*reversed(greater_numbers), sep=" ")



