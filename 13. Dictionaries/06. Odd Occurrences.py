words = input().split()
words_dict = {}

for i in words:
    word_to_check = i.lower()
    if word_to_check not in words_dict:
        words_dict[word_to_check] = 0
    words_dict[word_to_check] += 1

for (key, value) in words_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

