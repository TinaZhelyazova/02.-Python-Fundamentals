text = input()
letters = []

for i in range(len(text) - 1):
    if text[i] != text[i + 1]:
        letters.append(text[i])

#if text[-1] != text[-2]:
letters.append(text[-1])
print("".join(letters))

# aaaaabbbbbcdddeeeedssaa
