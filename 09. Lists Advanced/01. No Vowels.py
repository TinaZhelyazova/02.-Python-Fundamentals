text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
word = []

for i in text:
    if i.lower() not in vowels:
        word.append(i)

print("".join(word))
