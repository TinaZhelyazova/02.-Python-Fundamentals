sides = {}
is_in_list = []
line = input()

while True:

    if line == "Lumpawaroo":
        break

    if "|" in line:
        command = line.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side not in sides:
            sides[force_side] = []

        if force_user not in is_in_list:
            is_in_list.append(force_user)
            sides[force_side].append(force_user)

    else:
        command = line.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        if force_user in is_in_list:
            for key, value in sides.items():
                if force_user in value:
                    sides[key].remove(force_user)
                    sides[force_side].append(force_user)
                    print(f"{force_user} joins the {force_side} side!")
        if force_side in sides:
            if force_user not in is_in_list:
                is_in_list.append(force_user)
                sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
        else:
            if force_user not in is_in_list:
                sides[force_side] = []
                sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")

    line = input()

for key, value in sides.items():
    if len(value) >= 1:
        print(f"Side: {key}, Members: {len(value)}")
        for values in value:
            print(f"! {values}")
