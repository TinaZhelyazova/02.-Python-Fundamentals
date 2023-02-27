message = input().split(" ")
chipher = []

for word in message:
    digits = [ch for ch in word if ch.isdigit()]
    words_without_ints = [ch for ch in word if ch not in digits]
    conc_digits = ("".join(digits))
    int_to_str = chr(int(conc_digits))
    words_without_ints[0], words_without_ints[-1] = words_without_ints[-1], words_without_ints[0]
    new_words = int_to_str + "".join(words_without_ints)
    chipher.append(new_words)
print(' '.join(chipher))
