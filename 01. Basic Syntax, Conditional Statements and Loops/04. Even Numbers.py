number = int(input())

for i in range(number):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        break
if number%2 == 0:
    print("All numbers are even.")
    