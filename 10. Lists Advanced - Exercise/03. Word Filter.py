text = input().split(" ")
filtered = list(filter(lambda word: len(word) % 2 == 0, text))
print("\n".join(filtered))
