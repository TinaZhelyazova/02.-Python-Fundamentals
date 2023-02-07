numbers = [int(x) for x in input().split()]
n = int(input())

for i in range(n):
    number = min(numbers)
    numbers.remove(number)

print((", ").join([str(x) for x in numbers]))
