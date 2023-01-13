command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for i in command:
        print(f"{i}{i}", end="")

    print()
    command = input()
