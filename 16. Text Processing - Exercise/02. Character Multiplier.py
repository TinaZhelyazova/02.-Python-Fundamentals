strings = input().split(" ")
first_str = strings[0]
second_str = strings[1]
result = 0


if len(first_str) > len(second_str):
    for i in range(len(second_str)):
        result += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(second_str), len(first_str)):
        result += ord(first_str[i])
elif len(first_str) < len(second_str):
    for i in range(len(first_str)):
        result += ord(first_str[i]) * ord(second_str[i])
    for i in range(len(first_str), len(second_str)):
        result += ord(second_str[i])
elif len(first_str) == len(second_str):
    for i in range(len(first_str)):
        result += ord(first_str[i]) * ord(second_str[i])

print(result)
