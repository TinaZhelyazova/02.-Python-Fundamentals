number_of_rooms = int(input())
chair_counter = 0
chairs_needed = 0

for i in range(number_of_rooms):
    information = input().split(" ")
    number_of_chairs = information[0]
    number_of_visitors = information[1]

    if len(number_of_chairs) < int(number_of_visitors):
        print(f"{int(number_of_visitors)-len(number_of_chairs)} more chairs needed in room {i+1}")
        chairs_needed += 1
    elif len(number_of_chairs) == int(number_of_visitors):
        continue
    else:
        chair_counter += int(len(number_of_chairs)) - int(number_of_visitors)

if chairs_needed == 0:
    print(f"Game On, {chair_counter} free chairs left")
