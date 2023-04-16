from string import ascii_letters, digits
usernames = input().split(", ")
allowed_symbols = ascii_letters + digits + "_" + "-"
print_username = True


for username in usernames:
    print_username = True
    if len(username) < 3 or len(username) > 16:
        print_username = False
        continue

    for char in username:
        if char not in allowed_symbols:
            print_username = False
            continue
    if print_username:
        print(username)
