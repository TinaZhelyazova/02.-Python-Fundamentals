tail = input()
body = input()
head = input()

list_of_parts = [tail, body, head]

list_of_parts[0], list_of_parts[2] = list_of_parts[2], list_of_parts[0]

print(list_of_parts)
