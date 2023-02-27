numbers = list(map(int, input().split(" ")))
command = input().split(" ")
lst_numbers = list(numbers)

while True:
    if command[0] == "end":
        break

    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        lst_numbers[index1], lst_numbers[index2] = lst_numbers[index2], lst_numbers[index1]
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        result = lst_numbers[index1] * lst_numbers[index2]
        lst_numbers.pop(index1)
        lst_numbers.insert(index1, result)
    elif command[0] == "decrease":
        for i in range(len(lst_numbers)):
            lst_numbers[i] -= 1

    command = input().split(" ")

print(*lst_numbers, sep=", ")
