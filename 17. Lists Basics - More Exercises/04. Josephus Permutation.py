people = [int(x) for x in input().split()]
number = int(input())
executed_people = []
index = 0
while len(people) > 0:
    index = (index + number - 1) % len(people)

    executed_people.append(people[index])
    people.pop(index)

# Print the result list
print(executed_people)
