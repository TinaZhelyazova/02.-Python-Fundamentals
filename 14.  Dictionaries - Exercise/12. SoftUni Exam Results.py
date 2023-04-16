command = input()
data = {}

while True:

    if command == "exam finished":
        break

    username, language, points = command.split("-")

    data[username] = language, points

    if username in data:
        if language in data[username]:
            points = max(points)

    if command[1] == "banned":
        pass

print(data)
