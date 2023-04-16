phonebook = {}

while True:
    inpt = input()
    if inpt.isnumeric():
        for i in range(int(inpt)):
            searched_name = input()
            if searched_name not in phonebook:
                print(f"Contact {searched_name} does not exist.")
            else:
                print(f"{searched_name} -> {phonebook[searched_name]}")
        break
    entry = inpt.split("-")
    phonebook[entry[0]] = entry[1]







