txt = input()
digits = ""
string = ""
chars = ""

for i in txt:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        string += i
    else:
        chars += i

print(digits)
print(string)
print(chars)
