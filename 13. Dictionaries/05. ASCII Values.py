chars = input().split(", ")
#char_dict = {key: ord(key) for key in chars}
char_dict = {}

for key in chars:
    char_dict[key] = ord(key)

print(char_dict)
