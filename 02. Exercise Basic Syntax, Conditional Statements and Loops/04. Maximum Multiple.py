divisor = int(input())
boundary = int(input())
number = 0
previous_number = 0

for i in range(boundary, divisor, -1):
    if i % divisor == 0 and i > 0 and i <= boundary:
        number = i
        break

print(i)
