file_name = input().split("\\")
name = file_name[-1]
extension = name.split(".")
print(f"File name: {extension[0]}")
print(f"File extension: {extension[1]}")

