words = input().split(" ")
palindrome_word = input()

palindromes_in_words = []
palindrome_word_count = 0

for word in words:
    if word == "".join(reversed(word)):
        palindromes_in_words.append(word)

    if word == palindrome_word:
        palindrome_word_count += 1

print(palindromes_in_words)
print(f"Found palindrome {palindrome_word_count} times")
