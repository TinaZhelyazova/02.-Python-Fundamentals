numbers = [int(x) for x in input().split()]
text = input()
message = ""
for number in numbers:
    idx = 0
    for i in str(number):
        idx += int(i)
    idx = idx % len(text)
    message = message + (text[idx])
    text = text[:idx] + text[idx + 1:]

print(message)
