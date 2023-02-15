happiness = list(map(int, input().split(" ")))
factor = int(input())

mapped_numbers = list(map(lambda a: a * factor, happiness))
average = sum(mapped_numbers) / len(happiness)
counter = 0

for number in mapped_numbers:
    if number >= average:
        counter += 1

if counter >= len(happiness) // 2:
    print(f"Score: {counter}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(happiness)}. Employees are not happy!")
