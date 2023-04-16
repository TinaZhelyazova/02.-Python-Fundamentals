employee_inf = {}

while True:
    command = input()

    if command == "End":
        break

    args = command.split(" -> ")
    name = args[0]
    id = args[1]

    if name not in employee_inf:
        employee_inf[name] = []
        employee_inf[name].append(id)
    else:
        if id not in employee_inf[name]:
            employee_inf[name].append(id)



for key, value in employee_inf.items():
    print(f"{key}")
    for values in value:
        print(f"-- {values}", sep="\n")
