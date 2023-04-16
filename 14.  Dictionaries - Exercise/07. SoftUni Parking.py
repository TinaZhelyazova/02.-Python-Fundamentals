n = int(input())
database = {}

for i in range(n):
    args = input().split()

    if args[0] == "register":
        username = args[1]
        license_number = args[2]

        if username in database:
            print(f"ERROR: already registered with plate number {license_number}")
        else:
            database[username] = license_number
            print(f"{username} registered {license_number} successfully")
    elif args[0] == "unregister":
        username = args[1]
        if username not in database:
            print(f"ERROR: user {username} not found")
        else:
            database.pop(username)
            print(f"{username} unregistered successfully")
for key, value in database.items():
    print(f"{key} => {value}")
