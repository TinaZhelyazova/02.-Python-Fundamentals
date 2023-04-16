while True:
    strings = input()
    if strings == "end":
        break
    print(f"{strings} = {strings[::-1]}")
