text = input()
explosion = '>'
strength = 0
new_text = ''

for i in range(len(text)):
    if strength > 0 and text[i] != explosion:
        strength -= 1
        continue
    if text[i] != explosion:
        new_text += text[i]
    elif text[i] == explosion:
        strength += int(text[i+1])
        new_text += text[i]
        continue

print(new_text)

