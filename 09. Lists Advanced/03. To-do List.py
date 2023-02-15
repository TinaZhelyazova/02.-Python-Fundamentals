all_notes = []

while True:
    notes = input()

    if notes == "End":
        break

    split_commands = notes.split("-")
    importance = int(split_commands[0])
    task = split_commands[1]

    all_notes.append([importance, task])

sorted_tasks = [task_data[1] for task_data in sorted(all_notes)]

print(sorted_tasks)

