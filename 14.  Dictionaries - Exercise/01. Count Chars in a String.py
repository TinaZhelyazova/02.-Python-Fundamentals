char_input = input()
dict_chars = {}
words = char_input.replace(" ", "")
for char in words:
    if char not in dict_chars:
        dict_chars[char] = 0
    dict_chars[char] += 1

for (key,value) in dict_chars.items():
    print(f'{key} -> {value}')
