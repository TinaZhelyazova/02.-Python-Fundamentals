def chars_long(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def only_letters_and_digits(password):
    if password.isalnum():
        return True
    else:
        return False


def is_digit(password):
    digits = 0
    for i in password:
        if i.isdigit():
            digits += 1
    if digits >= 2:
        return True
    else:
        return False


#def is_not_valid(password):



input_password = input()
if chars_long(input_password) == True and only_letters_and_digits(input_password) == True and is_digit(input_password) == True:
    print(f"Password is valid")
if chars_long(input_password) == False:
    print(f"Password must be between 6 and 10 characters")
if only_letters_and_digits(input_password) == False:
    print("Password must consist only of letters and digits")
if is_digit(input_password) == False:
    print("Password must have at least 2 digits")
