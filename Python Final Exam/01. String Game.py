text = input()
new_text = ""

while True:
    command = input().split()

    if command[0] == "Done":
        break

    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in text:
            print("True")
        else:
            print("False")

    elif command[0] == "End":
        substring = command[1]
        if text.endswith(substring):
            print("True")
        else:
            print("False")
    elif command[0] == "Uppercase":
        text = text.upper()
        print(text)

    elif command[0] == "FindIndex":
        char = command[1]
        index_of_char = text.index(char)
        print(index_of_char)

    elif command[0] == "Cut":
        start_index = int(command[1])
        count_index = int(command[2])
        counter = count_index
        text = text[start_index: -1: 1]
        new_text = ""
        for i in range(count_index):
            new_text += text[i]
            counter -= 1
            if counter == 0:
                print("".join(new_text))
