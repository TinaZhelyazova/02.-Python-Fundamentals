import re

n = int(input())

for i in range(n):
    string = input()

    # check if the string matches the valid format
    if re.match(r'![A-Z][a-z]+!+:\[[A-Za-z0-9]+]$', string) and len(string) >= 8:
        command = string.split(':')[0][1:-1]
        text = string.split('[')[1][:-1]
        if len(text) < 8:
            print("The message is invalid")
            continue
        numbers = [str(ord(ch)) for ch in text]

        # output the result in the required format
        result = f"{command}: {' '.join(numbers)}"
        print(f"{result}")
    else:
        print("The message is invalid")

