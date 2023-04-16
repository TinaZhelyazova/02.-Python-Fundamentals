text = input()
encrypted_text = []

for char in text:
    encrypted_char = ord(char) + 3
    caesar_char = chr(encrypted_char)
    encrypted_text.append(caesar_char)

print("".join(encrypted_text))
