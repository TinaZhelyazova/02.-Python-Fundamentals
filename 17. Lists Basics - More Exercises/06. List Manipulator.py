lst = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break
    else:
        command = command.split()

        if command[0] == "exchange":
            index = int(command[1])
            if index > len(lst) or index < 0:
                print("Invalid index")
            else:
                lst = lst[index + 1:]+lst[0:index + 1]

        elif command[0] == "max" or command[0] == "min":
            number = 0
            if command[1] == "even":
                if not [x for x in lst if x % 2 == 0]:  # ако няма четни числа принтирай:
                    print("No matches")
                    continue
                else:
                    if command[0] == "max":
                        number = max([x for x in lst if x % 2 == 0])  # намираме максималното число на четните числа
                    elif command[0] == "min":
                        number = min([x for x in lst if x % 2 == 0])  # намираме минимума на четните числа

            elif command[1] == "odd":
                if not [x for x in lst if x % 2 == 1]:  # ако няма нечетни числа принтирай:
                    print("No matches")
                    continue
                else:
                    if command[0] == "max":
                        number = max([x for x in lst if x % 2 == 1])  # намираме макса на нечетните числа
                    elif command[0] == "min":
                        number = min([x for x in lst if x % 2 == 1])  # намираме минимума на нечетните числа

            if lst.count(number) > 1:  # count returns the number of times "number" appear in the list
                for i in range(len(lst) - 1, -1, -1):  # започваме броенето отзад напред, за да намерим първото
                    # най-голямо или най-малко число от дясно наляво
                    if lst[i] == number:
                        print(i)
                        break
            else:
                print(lst.index(number))

        elif command[0] == "first" or command[0] == "last":
            count = int(command[1])
            new_list = []

            if count > len(lst):
                print("Invalid count")
                continue
            else:
                if command[2] == "even": # list with even nums only
                    new_list = [x for x in lst if x % 2 == 0]
                elif command[2] == "odd": # list with odd nums only
                    new_list = [x for x in lst if x % 2 == 1]

                if command[0] == "first":
                    new_list = new_list[:count]
                    print(new_list)
                elif command[0] == "last":
                    if len(new_list) <= count:
                        print(new_list)
                    else:
                        new_list = new_list[len(new_list)-count:]
                        print(new_list)

print(lst)

