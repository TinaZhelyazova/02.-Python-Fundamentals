number_of_wagons = int(input())
train = [0] * number_of_wagons
command = input().split(" ")

while command[0] != "End":
    if command[0] == "add":
        number_of_people_added = int(command[1])
        train[-1] += number_of_people_added
    elif command[0] == "insert":
        number_of_wagon = int(command[1])
        number_of_people = int(command[2])
        train[number_of_wagon] += number_of_people
    elif command[0] == "leave":
        number_of_wagon = int(command[1])
        number_of_people = int(command[2])
        train[number_of_wagon] -= number_of_people

    command = input().split(" ")

print(train)
