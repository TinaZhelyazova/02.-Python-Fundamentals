strings = input().split(" ")
result = {string * len(string) for string in strings}
print(" ". join(result))

