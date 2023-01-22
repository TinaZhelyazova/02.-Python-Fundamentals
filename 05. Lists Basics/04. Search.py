n = int(input())
word = input()
list_of_texts = []
filtered_text = []

for i in range(n):
    curr_text = input()
    list_of_texts.append(curr_text)
    if word in curr_text:
        filtered_text.append(curr_text)

print(list_of_texts)
print(filtered_text)

