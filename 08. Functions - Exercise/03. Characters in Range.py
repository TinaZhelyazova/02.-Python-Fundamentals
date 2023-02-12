def characters(start, end):
    for i in range(ord(start)+1, ord(end)):
        chars.append(chr(i))
    return chars


start_char = input()
end_char = input()
chars = []
print(" ". join(characters(start_char, end_char)))
